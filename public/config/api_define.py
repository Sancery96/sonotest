#!/usr/bin/env python
# -*- coding: utf-8 -*-
#2015.12.20 maol
import random

from annot_config import annot_event
from bdmk_config import bdmk_event
from panel_config import panel_event, panel_event1
from probe_config import probe_list
from screen_config import screen_event, screen_event1
from stdkey_config import stdkey_event, special_key, blank_key

server_return = "playback"

#maol,2016,02,03
#读取录制的文件并进行用例转换,
#词条注释与体标注释的三种不同情形的逻辑转换
#参数分别为1，2，4列时的不同逻辑转换
def from_record_to_case(src_file_name, dst_file_name):
    pass
    src_file = open(src_file_name, "r")
    dst_file = open(dst_file_name, "w")
    for line in src_file:
        if line.startswith("time.") or line.startswith("client.") :
            dst_file.write(line)
            continue

        line = line.replace("\n", "")
        linedata = line.split(',') #逗号分割
        colm = len(linedata)
        if colm == 1:
            num=linedata[0]
            for i in range(0,len(panel_event)):
                if str(panel_event.values()[i]) == str(num):
                    panelkey = str(panel_event.keys()[i])
                    dst_file.write("client.simple_event('%s')\n" % panelkey)
                    break
        elif colm == 2: #标准按键
                num = linedata[0]
               # num = hex(int(num)) #16进制
                for i in range(0, len(stdkey_event)):
                    if num == str(stdkey_event.values()[i]):
                        key_name = stdkey_event.keys()[i]
                        out_str = ""
                        if key_name in special_key or key_name in blank_key:
                            out_str = "client.key_event('%s')\n" % key_name
                        else:
                            key_str = num = linedata[1].strip()
                            if key_str == "\"" or  key_str == "\'":
                                out_str = "client.key_event('\%s')\n" % key_str
                            else:
                                out_str = "client.key_event('%s')\n" % key_str
                        if out_str != "":
                            dst_file.write(out_str)
                        break
        elif colm == 3: #touch screen event
            num = linedata[0]
            #TGC format: <TGC ID>, <TGC index>, <TGC value>
            if num.isdigit() and int(num) == panel_event['TGC']:
                dst_file.write("client.simple_event('%s', %s, %s)\n" % ('TGC', linedata[1].strip(), linedata[2].strip()))
            elif num.isdigit() and int(num) == screen_event['LGC_VALUE'][0]:
                dst_file.write("client.LGC_adjust('%s', %s, %s)\n" % ('LGC_VALUE', linedata[1].strip(), linedata[2].strip()))
            elif not num.isdigit():
                dst_file.write("client.adjust_param('%s', '%s', '%s')\n" % (num, linedata[1].strip(), linedata[2].strip()))
                #linedata = [int(x) for x in linedata]
                #for i in range(len(screen_event)):
                    #if screen_event.values()[i] == linedata:
                        #dst_file.write("client.adjust_param('%s')\n" % screen_event.keys()[i] )
        #touchscreen measure
        elif colm == 4:
            measure_section = linedata[0]
            measure_id = linedata[1]
            measure_side = linedata[2]
            measure_step = linedata[3]
            dst_file.write("client.touchscreen_measure(%s, %s, %s, %s)\n" % (measure_section, measure_id, measure_side, measure_step))

    src_file.close()
    dst_file.close()

#for simple_event
MOUSE_UP = 0x4802
KEY_UP = 0x4805
KEY_DOWN = 0x4804
MOUSE_BUTTON_RELEASE=18434
MOUSE_MOVE = 18432
#for simple_event

L_SET = 0
R_SET = 1

# return status
RETURN_SUCCESS = 0
RETURN_FAIL = 1
RETURN_ASSERT = 2
RETURN_STOP_PLAYBACK = 3
RETURN_NOT_SUPPORT = 4

# func return
RETURN_FUNC = 100
RETURN_LED_CLOSE = RETURN_FUNC
RETURN_LED_WHITE = RETURN_LED_CLOSE + 1
RETURN_LED_YELLOW = RETURN_LED_WHITE + 1

not_support_probe_list = []

class WrapClient:

    def __init__(self, client):
        self.internal_client_ = client
        self.sw_version = self.internal_client_.get_sw_version()
        self.return_from_server = 0
        self.casename = ""
        self.runflag = 1 #^^ 2016.9.21 add by zhengyj fixed timeout can not stop
        print("server version is %s" % self.sw_version)

    def _handle_return_from_event(self, result):
        global server_return
        if RETURN_STOP_PLAYBACK == result:
            print("stop playback")
            server_return = "quit"
        elif RETURN_ASSERT == result:
            print("got assert from server")
            server_return = "assert"
        elif RETURN_SUCCESS == result:
            #print "handled event"
            pass
        elif RETURN_FAIL == result:
            #print "unhandled event"
            pass
        elif RETURN_NOT_SUPPORT == result:
            #print "not support event"
            server_return = "not support"
        elif RETURN_LED_CLOSE == result:
            server_return = "LED close"
        elif RETURN_LED_WHITE == result:
            server_return = "LED white"
        elif RETURN_LED_YELLOW == result:
            server_return = "LED yellow"       

    def key_event(self, name):
        tmp = name.strip()
        tmp = name.upper()
        if tmp in stdkey_event.keys():
            if tmp in special_key:
                self.return_from_server = self.internal_client_.key_event(stdkey_event[tmp], special_key[tmp])
            elif tmp in blank_key:
                self.return_from_server = self.internal_client_.key_event(stdkey_event[tmp], "")
            else:
                self.return_from_server = self.internal_client_.key_event(stdkey_event[tmp], name)
        self._handle_return_from_event(self.return_from_server)

    #面板按键接口#
    def simple_event(self, name, wparam=-1, lparam=-1, msg = int(KEY_DOWN)):
        self.return_from_server = 1
        name = name.strip()
        name = name.upper()
        # if simple_event("TGC"),change it to simple_event("TGC"+"[1-8]")
        if name == "TGC" and (wparam==-1 or lparam==-1):
            value_str = str(random.randint(1,8))
            name = name+value_str
        if name in panel_event1.keys():
            self.return_from_server = self.internal_client_.panel_event(msg, panel_event1[name], wparam, lparam)
        elif name=="L_SET":  #press and release
            self.return_from_server = self.internal_client_.mousebutton_event(int(MOUSE_UP), 0)
        elif name=="R_SET":
            self.return_from_server = self.internal_client_.mousebutton_event(int(MOUSE_UP), 1)
        elif (len(name) == 4) and name.startswith("TGC"):
            key = name[0:3]
            index = int(name[-1]);
            value = random.randint(0, 255)
            if index < 9:
                if key in panel_event1:
                   self.return_from_server = self.internal_client_.TGC_adjust(int(KEY_DOWN) , panel_event1[key] , index ,value)
                else:
                    print("error! cannot find %s in panel_config! " % key)
            else:
                print("error! Invalid TGC param :%s " % name)
        else:
            self.return_from_server = self.internal_client_.panel_event(msg, name, wparam, lparam)
            #print "error! cannot find %s in panel_config! or Invalid TGC param " % name

        self._handle_return_from_event(self.return_from_server)

    #参数调节接口#
    def adjust_param(self, name, wparam=-1, lparam=-1):
        name = name.strip()
        if name in screen_event1.keys():
            self.return_from_server = self.internal_client_.param_adjust(screen_event1[name][0],screen_event1[name][1],screen_event1[name][2])
        else:
            self.return_from_server = self.internal_client_.param_adjust(name, wparam, lparam)
            #print "error! cannot find %s in screen_config! " % name
        self._handle_return_from_event(self.return_from_server)

    #鼠标相对移动接口#
    def mousemove_rel_event(self, x, y):
        self.return_from_server = 1
        self.return_from_server = self.internal_client_.mousemove_rel_event(x, y)
        self._handle_return_from_event(self.return_from_server)

    def mousemove_to_event(self, x, y):
        self.return_from_server = 1
        self.return_from_server = self.internal_client_.mousemove_to_event(x, y)
        self._handle_return_from_event(self.return_from_server)

    #词条注释接口#
    def annot_event(self,name):
        self.return_from_server = 1
        count=0
        if name.endswith('_ONE'):
            name=name[0:-4]
            if name in annot_event:
                rindex=random.randint(0,16)
                cindex=random.randint(0,1)
                self.return_from_server = self.internal_client_.Comment_BDMK_event(True,False,False,rindex,cindex)
        elif name.endswith('_ALL'):
            for rindex in range(0,17):
                for cindex in range(0,2):
                    self.return_from_server = self.internal_client_.Comment_BDMK_event(True,False,False,rindex,cindex)
        #                    self.internal_client_.mousebutton_event(int(MOUSE_UP),0)

        elif("application" == name.lower()):
            self.return_from_server = self.internal_client_.Comment_BDMK_event(True,True,False,255,255)
        else:
            self.return_from_server = self.internal_client_.Comment_BDMK_event(True,True,True,annot_event[name],255)

        self._handle_return_from_event(self.return_from_server)

    #体标注释接口#
    def bdmk_event(self,name):
        self.return_from_server = 1
        if name.endswith('_ONE'):
            name=name[0:-4]
            if name in bdmk_event:
                rindex=random.randint(0,6) #random uses <=&>=
                cindex=random.randint(0,2)
                self.return_from_server = self.internal_client_.Comment_BDMK_event(False,False,False,rindex,cindex)
        elif name.endswith('_ALL'):
            for rindex in range(0,7):
                          for cindex in range(0,3): #range uses <
                              self.internal_client_.Comment_BDMK_event(False,False,False,rindex,cindex)
        #            self.internal_client_.mousebutton_event(int(MOUSE_UP),0)
        elif ("application" == name.lower()):
            self.return_from_server = self.internal_client_.Comment_BDMK_event(False,True,False,255,255)
        else:
            self.return_from_server = self.internal_client_.Comment_BDMK_event(False,True,True,bdmk_event[name],255)

        self._handle_return_from_event(self.return_from_server)

    def enter_exam(self, probe_index, exam_index):
        #self.return_from_server = 1
        #print probe_index, exam_index
        self.return_from_server = self.internal_client_.enter_exam(probe_index, exam_index)
        self._handle_return_from_event(self.return_from_server)

    #虚拟探头接口 2016.02.25#
    def force_probe(self,ProbeName):
        EndForce_flag=False
        ProbeName=ProbeName.upper()
        #add by zyj for probe is id will be ok too
        if ProbeName.isdigit():
            ProbeID = int(ProbeName)
            if ProbeID == 0 or ProbeID == -1:
                EndForce_flag = True
            self.return_from_server = self.internal_client_.force_probe(ProbeID,EndForce_flag)
        elif ProbeName not in probe_list.keys():
            print("error, cannot find Probe =%s in %s" % (ProbeName, probe_list))
            self.return_from_server = RETURN_NOT_SUPPORT
        else:
            ProbeID=probe_list[ProbeName]  #get probeID in probetable
            if  ProbeName=="END":
                EndForce_flag=True
            self.return_from_server = self.internal_client_.force_probe(ProbeID,EndForce_flag)

        # 不支持的探头记录到列表
        global not_support_probe_list
        if self.return_from_server == RETURN_NOT_SUPPORT and ProbeName not in not_support_probe_list:
            not_support_probe_list.append(ProbeName)

        self._handle_return_from_event(self.return_from_server)

    def getAllExam(self,probeID):
        myfile = open("./AllExam2probe",'a')
        exams = self.internal_client_.getAllExam(int(probeID.strip()))
        tmpstr = ""
        for key in probe_list.keys():
            if probe_list[key] == int(probeID):
                tmpstr = key + ":" + exams + "\n"
        myfile.write(tmpstr)
        myfile.close()
    #存储当前图片接口 传输当前执行的脚本名称
    #为区分截屏的顺序操作，需要将.case文件的当前代码行数发送给服务端，让服务端截屏存储图片时，用当前代码行数命名图片
    def save_current_screen(self, linenum=0):
        print(self.casename)
        self.return_from_server = self.internal_client_.save_current_screen(self.casename, linenum)
        self._handle_return_from_event(self.return_from_server)

    def mouse_press_event(self, button):
        if button == "L_SET":            
            self.return_from_server = self.internal_client_.mouse_press_event(L_SET)
        elif button == "R_SET":
            self.return_from_server = self.internal_client_.mouse_press_event(R_SET)
        else:
            return

        self._handle_return_from_event(self.return_from_server)

    def mouse_release_event(self, button):
        if button == "L_SET":            
            self.return_from_server = self.internal_client_.mouse_release_event(L_SET)
        elif button == "R_SET":
            self.return_from_server = self.internal_client_.mouse_release_event(R_SET)
        else:
            return

        self._handle_return_from_event(self.return_from_server)        

    def LGC_adjust(self, name, index, value):
        self.return_from_server = 1
        name = name.strip()
        if name in screen_event1.keys():
            self.return_from_server = self.internal_client_.LGC_adjust( screen_event1[name][0], index, value )        
        self._handle_return_from_event(self.return_from_server)

    def touchscreen_measure(self, section, id, side, step):
        self.return_from_server = self.internal_client_.touchscreen_measure(section, id, side, step)
        self._handle_return_from_event(self.return_from_server)

    def get_led_status(self, func_name):
        if func_name in panel_event1.keys():
            self.return_from_server = self.internal_client_.get_led_status(panel_event1[func_name])
        elif func_name in panel_event1.values():
            self.return_from_server = self.internal_client_.get_led_status(func_name)
        else:
            self.return_from_server  = -1
        return self.return_from_server	

