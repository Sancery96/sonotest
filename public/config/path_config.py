# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: path_config.py
@time: 2022/2/9 22:02
@usage: 
"""

remoteServerIP = '192.168.93.70'
username = 'root'
password = '123456'

# global ssh
# ssh = SSHClient.Client(remoteServerIP, username, password)

# mea_root_path = r'/home/tony/VistaSB/proj/start/02-data/rw/measure/config/measure/xmlconfig/measurement/'
mea_root_path = r'/home/tony/02-data/series/ro/measure/config/measure/xmlconfig/measurement/'
# mea_menu_root_path = mea_root_path + r'Menu/'
mea_menu_root_path = mea_root_path + r'Menu/Default/'
mea_comb_root_path = mea_root_path + r'Combine/'
mea_menu_memory_file_path = mea_menu_root_path + 'MenuMemory.xml'

pdb_root_path = r'/home/tony/VistaSB/proj/start/02-data/rw/system/probetable/'

point_range_dict = {'KW_DISTANCE': {'x1': 478, 'y1': 133, 'x2': 1222, 'y2':867}}

zh_dict = {'pw实时':['pw','update'],
           '自动包络':['autotrace'],
           'CW自动包络':['cw_autotrace'],
           '同步':['pw_simult'],
           '调大基线':['baseline_up'],
           '调小基线':['baseline_down'],
           '冻结':['freeze'],
           '解冻':['freeze'],
           '专业测量':['calc'],
           '基础测量':['caliper'],
           '注释': ['annot'],
           '体标': ['bodymark'],
           '报告':['report'],
           'B+CFM+CW':['b','c','cw','update'],}

ui_coord_dict = {'sys_apply':(247,985),
                 'sys_exit':(247,1029),
                 'sys_check':(254,238),

                 'sys_measure':(578,123),
                 'sys_mea_list':(750,172),
                 'sys_mea_calc':(903,172),
                 'sys_mea_calc_draw1':(572,240),
                 'sys_mea_calc_card':(454,396),
                 'sys_mea_calc_new':(589,443),

                  'sys_freeze_resp_draw':(1116,541),
                  'sys_freeze_resp_cine': (1000, 578),
                  'sys_freeze_resp_annotation': (1000, 616),
                  'sys_freeze_resp_calc': (1000, 658),
                  'sys_freeze_resp_bodymark': (1000, 692),
                  'sys_freeze_resp_arrow': (1000, 730),
                  'sys_freeze_resp_caliper': (1000, 765),

                  'repo_abd':(),
                  'repo_ob':(),
                  'repo_gyn':(),
                  'repo_card':(),
                  'repo_vas':(),
                  'repo_uro':(),
                  'repo_smp':(),
                  'repo_ped':(),
                  'repo_left1':(241, 125),
                  'repo_left2': (241, 180),
                  'repo_left3': (241, 235),
                  'repo_left4': (241, 290),
                 'repo_left5': (241, 125),
                 'repo_left6': (241, 180),
                 'repo_left7': (241, 235),
                 'repo_left8': (241, 290),

                 'review_patient_list':(258, 967),
                 'review_text':(1056, 123),
                 'review_item_draw':(910, 121),
                 'review_item_patient_id':(650, 200),

                 'clipboard1':(1670,220),
                 'clipboard2':(1840,220),
                 'clipboard3': (1670, 360),
                 'clipboard4': (1840, 360),
                 'clipboard5': (1670, 500),
                 'clipboard6': (1840, 500),
                 'clipboard7': (1670, 640),
                 'clipboard8': (1840, 640),
                 'clipboard9': (1670, 780),
                 'clipboard10': (1840, 780),
                 'clipboard11': (1670, 920),
                 'clipboard12': (1840, 920),
                 }

command_dict = {'KW_ACCELERATION' : 2,              #   加速度
                'KW_ALTRACE' : 2,                   #
                'KW_ANGLE': 3,                      #   3点测角
                'KW_ANGLE2L': 4,                    #   直线夹角
                'KW_ANGLE2LPF': 2,                  #   盆底直线夹角
                'KW_ANGLEPF': 2,                    #   盆底3点测角
                'KW_AUTO_AC': 2,
                'KW_AUTO_BLADDER_TRACE':1,
                'KW_AUTO_BPD': 2,
                'KW_AUTO_DISKREGION' : 2,
                'KW_AUTO_FL': 2,
                'KW_AUTO_FOLLICLE_2D': 2,
                'KW_AUTO_HC': 2,
                'KW_AUTO_HL': 2,
                'KW_AUTO_NT': 2,
                'KW_AUTO_PF_TRACE' : 2,
                'KW_AUTO_PF_TRACE_3D': 2,
                'KW_AUTO_TRACE_AC': 2,
                'KW_AUTO_TRACE_HC': 2,
                'KW_AUTO_UTERUS' : 2,
                'KW_BEZIERLENGTH' : 2,
                'KW_COLOR_FLOW' : 2,
                'KW_COLOR_FLOWVELOCITY' : 2,
                'KW_CONTRASTELLIPSE' : 2,
                'KW_CONTRASTTRACE' : 2,
                'KW_D_THITA': 2,
                'KW_DHR': 2,
                'KW_DISK_REGION' : 2,
                'KW_DISTANCE': 2,
                'KW_DISTANCEFOURPT': 2,
                'KW_DPDT' : 2,
                'KW_DTIME': 2,
                'KW_DVELOCITY': 2,
                'KW_ELASTICELLIPSE' : 2,
                'KW_ELASTICTRACE' : 2,
                'KW_ELLIPSE': 3,
                'KW_ELLIPSEEX': 2,
                'KW_FREEZE_AUTO_TRACE': 2,
                'KW_HIP': 2,
                'KW_HIP_Dd': 3,
                'KW_HIP_DE' : 2,
                'KW_HIP_GRAF' : 2,
                'KW_HIP3D': 2,
                'KW_IMT' : 2,
                'KW_LINE2D': 3,
                'KW_MANUAL_TRACE': 2,
                'KW_MDISTANCE': 2,
                'KW_MDISTANCEFOURPT' : 2,
                'KW_MHR': 2,
                'KW_MSLOPE' : 2,
                'KW_MTIME': 2,
                'KW_PHT' : 2,
                'KW_POINTAREA': 2,
                'KW_POLYLINE_DISTANCE': 2,
                'KW_REAL_TIME_AUTO_TRACE' : 2,
                'KW_SEMI_AUTO_TRACE': 2,
                'KW_TRACE': 2,
                'KW_TRACELENGTH': 2,
                }

probe_dict = {
            "C311" : 82142,
            "C322" : 52112,
            "C344" : 112142,
            "BCC9-5" : 212142,
            "C353" : 97142,
            "C354" : 102142,
            "C362" : 222142,
            "C542" : 107142,
            "C611" : 137142,
            "C613" : 242142,
            "3C-A" : 142112,
            "C1-5" : 112107,
            "C544" : 147142,
            "C356" : 247142,
            "C1-6" : 107112,
            "C1-6A" : 57112,
            "C2-9" : 242112,
            "C3-10V" : 247112,
            "L741" : 172142,
            "L742" : 182142,
            "L743" : 177142,
            "L752" : 187142,
            "10L1" : 197142,
            "LAP7" : 192142,
            "10I2" : 207142,
            "12L-A" : 72112,
            "10I3" : 237142,
            "10L-I" : 177112,
            "12L-B" : 132112,
            "13L-A" : 42112,
            "18L-A" : 237112,
            "12LI-A" : 77112,
            "12LT-A" : 87112,
            "9L-A" : 162142,
            "3P1" : 67142,
            "2P1" : 62142,
            "2P2" : 57142,
            "5P2" : 77142,
            "8P1" : 87142,
            "3P2" : 227142,
            "5P1" : 52142,
            "4P-A" : 122112,
            "S1-6" : 112102,
            "7P-A" : 112112,
            "P5-1" : 47142,
            "6V1" : 127142,
            "6V3" : 122142,
            "6V7" : 187112,
            "6V1A" : 132142,
            "6V3A" : 192112,
            "6CI-A" : 82112,
            "6CT-A" : 92112,
            "MPTEE" : 37142,
            "MPTEEMINI" : 27142,
            "CWD2.0" : 82082,
            "CW4.0" : 77077,
            "PW2.0" : 247247,
            "EC9-5" : 117142,
            "BCL10-5" : 217142,
            "12C-ER" : 197112,
            "VC6-2OLD" : 92142,
            "VL12-5" : 167142,
            # "VE9-5" : 202142,
            "VC6-2" : 212112,
            "VC2-9" : 227112,
            "VE3-10" : 222112,
            "VC2-9A" : 37112,
            "VE9-5" : 207112,
            "CWD5.0" : 77077,
            "CWD8.0" : 92092,
            "C345" : 142142,
            "12L-I" : 182112,
            "L741V" : 252142,
            "3P-A" : 202112,
            "ERC12-5" : 152142,
            "S1-5" : 102112,
            "EG-UR5" : 47112,
            "7P-B" : 97112,
            "6V3AOLD" : 132157,
            "ML3-18": 172112,
            "13L-B": 67112,
            "EG-UC5T":232142,
            "END":255255
              }

exam_dict = {0: {'id': '0', 'application': 'KW_VASCULAR', 'category': 'KW_VR_CAROTID', 'collection': ''},
             1: {'id': '1', 'application': 'KW_SMP', 'category': 'KW_THYROID', 'collection': ''},
             2: {'id': '2', 'application': 'KW_SMP', 'category': 'KW_BREAST', 'collection': ''},
             3: {'id': '3', 'application': 'KW_VASCULAR', 'category': 'KW_VR_LEART', 'collection': ''},
             4: {'id': '4', 'application': 'KW_CARDIAC', 'category': 'KW_CARDIAC', 'collection': ''},
             5: {'id': '5', 'application': 'KW_ABDOMEN', 'category': 'KW_ABDOMEN', 'collection': ''},
             6: {'id': '6', 'application': 'KW_URINARY', 'category': 'KW_URINARY', 'collection': ''},
             7: {'id': '7', 'application': 'KW_OB', 'category': 'KW_BIOMETRY_CATE', 'collection': 'KW_FETALBIOMETRY'},
             8: {'id': '8', 'application': 'KW_ABDOMEN', 'category': 'KW_ABDOMEN', 'collection': ''},
             9: {'id': '9', 'application': 'KW_URINARY', 'category': 'KW_URINARY', 'collection': ''},
             10: {'id': '10', 'application': 'KW_ABDOMEN', 'category': 'KW_ABDOMEN', 'collection': ''},
             11: {'id': '11', 'application': 'KW_ABDOMEN', 'category': 'KW_ABDOMEN', 'collection': ''},
             12: {'id': '12', 'application': 'KW_GYN', 'category': 'KW_GYN', 'collection': ''},
             13: {'id': '13', 'application': 'KW_URINARY', 'category': 'KW_URINARY', 'collection': ''},
             14: {'id': '14', 'application': 'KW_SMP', 'category': 'KW_THYROID', 'collection': ''},
             15: {'id': '15', 'application': 'KW_URINARY', 'category': 'KW_URINARY', 'collection': ''},
             16: {'id': '16', 'application': 'KW_URINARY', 'category': 'KW_URINARY', 'collection': ''},
             17: {'id': '17', 'application': 'KW_VASCULAR', 'category': 'KW_VR_UEART', 'collection': ''},
             18: {'id': '18', 'application': 'KW_VASCULAR', 'category': 'KW_VR_LEART', 'collection': ''},
             19: {'id': '19', 'application': 'KW_ABDOMEN', 'category': 'KW_ABDOMEN', 'collection': ''},
             20: {'id': '20', 'application': 'KW_ABDOMEN', 'category': 'KW_ABDOMEN', 'collection': ''},
             21: {'id': '21', 'application': 'KW_SMP', 'category': 'KW_TESTICLE', 'collection': ''},
             22: {'id': '22', 'application': 'KW_VASCULAR', 'category': 'KW_VR_LEART', 'collection': ''},
             23: {'id': '23', 'application': 'KW_OB', 'category': 'KW_BIOMETRY_CATE', 'collection': 'KW_EARLYGEST'},
             24: {'id': '24', 'application': 'KW_PAEDIATRICS', 'category': 'KW_PAEDIATRICS',
                  'collection': 'KW_PAEDIATRICS_HIP'},
             25: {'id': '25', 'application': 'KW_SMP', 'category': 'KW_THYROID', 'collection': ''},
             26: {'id': '26', 'application': 'KW_VASCULAR', 'category': 'KW_VR_LEVENOUS', 'collection': ''},
             27: {'id': '27', 'application': 'KW_OB', 'category': 'KW_BIOMETRY_CATE', 'collection': 'KW_EARLYGEST'},
             28: {'id': '28', 'application': 'KW_GYN', 'category': 'KW_GYN',
                  'collection': 'MEASURE_MEA_GROUP_GYN_B_PF_BND'},
             29: {'id': '29', 'application': 'KW_ABDOMEN', 'category': 'KW_ABDOMEN', 'collection': ''},
             30: {'id': '30', 'application': 'KW_PAEDIATRICS', 'category': 'KW_PAEDIATRICS', 'collection': ''},
             31: {'id': '31', 'application': 'KW_VASCULAR', 'category': 'KW_VR_TCD', 'collection': ''},
             32: {'id': '32', 'application': 'KW_ABDOMEN', 'category': 'KW_ABDOMEN', 'collection': ''},
             33: {'id': '33', 'application': 'KW_OB', 'category': 'KW_FETALHEART_CATE', 'collection': ''},
             34: {'id': '34', 'application': 'KW_ABDOMEN', 'category': 'KW_ABDOMEN', 'collection': ''},
             35: {'id': '35', 'application': 'KW_OB', 'category': 'KW_BIOMETRY_CATE', 'collection': 'KW_FETALBIOMETRY'},
             36: {'id': '36', 'application': 'KW_VASCULAR', 'category': 'KW_VR_CAROTID', 'collection': ''},
             37: {'id': '37', 'application': 'KW_VASCULAR', 'category': 'KW_VR_UEVENOUS', 'collection': ''},
             38: {'id': '38', 'application': 'KW_ABDOMEN', 'category': 'KW_ABDOMEN', 'collection': ''},
             40: {'id': '40', 'application': 'KW_OB', 'category': 'KW_FETALHEART_CATE', 'collection': ''},
             41: {'id': '41', 'application': 'KW_GYN', 'category': 'KW_GYN',
                  'collection': 'MEASURE_MEA_GROUP_GYN_B_PF_BND'},
             42: {'id': '42', 'application': 'KW_GYN', 'category': 'KW_GYN',
                  'collection': 'MEASURE_MEA_GROUP_GYN_B_PF_BND'},
             43: {'id': '43', 'application': 'KW_GYN', 'category': 'KW_GYN',
                  'collection': 'MEASURE_MEA_GROUP_GYN_B_PF_BND'}}

panel_button_dict = {# 通用按键
                    'probe':'PROBE',	                    #切换到探头界面	client.simple_event('PROBE')
                    'freeze':'FREEZE',	                    #冻结/恢复图像	client.simple_event("FREEZE")
                    'depth_up':'DEPTH_UP',	                #调高扫描深度	client.simple_event('DEPTH_UP')
                    'depth_down':'DEPTH_DOWN',	            #调低扫描深度	client.simple_event('DEPTH_DOWN')
                    'zoom':'ZOOM',	                        #放大键	client.simple_event('ZOOM')
                    'zoom_right':'ZOOM_RIGHT',	            #放大图像	client.simple_event('ZOOM_RIGHT')
                    'zoom_left':'ZOOM_LEFT',	            #缩小图像	client.simple_event('ZOOM_LEFT')
                    'scale_up':'SCALE_UP',	                #调大脉冲重复频率	client.simple_event('SCALE_UP')
                    'scale_down':'SCALE_DOWN',	            #调小脉冲重复频率	client.simple_event('SCALE_DOWN')
                    'single':'SINGLE',	                    #单幅显示	client.simple_event('SINGLE')
                    'dual':'DUAL',	                        #双幅显示	client.simple_event('DUAL')
                    'quad':'QUAD',	                        #四幅显示	client.simple_event('QUAD')
                    'caliper':'CALIPER',	                #激活基础测量键	client.simple_event('CALIPER')
                    'calc':'CALC',	                        #激活应用测量键	client.simple_event('CALC')
                    'pointer':'POINTER',	                #轨迹球功能转换键	client.simple_event('POINTER')
                    'report':'REPORT',	                    #进入或退出患者报告界面	client.simple_event('REPORT')
                    'review':'REVIEW',	                    #预览键	client.simple_event('REVIEW')
                    'patient':'PATIENT',	                #进入患者信息界面	client.simple_event('PATIENT')
                    'image':'IMAGE',	                    #图像保存键	client.simple_event('IMAGE')
                    'auto':'AUTO',	                        #自动优化键	client.simple_event('AUTO')
                    'cine':'CINE',	                        #电影保存键	client.simple_event('CINE')
                    'update':'UPDATE',	                    #刷新键	client.simple_event("UPDATE")
                    'baseline_up':'BASELINE_UP',	        #调大基线位置	client.simple_event('BASELINE_UP')
                    'baseline_down':'BASELINE_DOWN',	    #调小基线位置	client.simple_event('BASELINE_DOWN')
                    'end_exam':'END_EXAM',	                #结束诊断键	client.simple_event('END_EXAM')
                    'endexam': 'END_EXAM',
                    'bdmk':'BDMK',	                        #体位标记键	client.simple_event('BDMK')
                    'bodymark': 'BODY_MARK_RIGHT',
                    'arrow':'ARROW',	                    #箭头标记键	client.simple_event("ARROW")
                    'annot':'ANNOT',	                    #注释键	client.simple_event("ANNOT")
                    'clear':'CLEAR',	                    #清屏按键	client.simple_event("CLEAR")
                    'point': 'POINTER',
                    'l_set': 'L_SET',
                    'r_set': 'R_SET',
                    # B模式
                    'b':'B',	                            #进入B模式	client.simple_event("B")
                    'b_left':'B_LEFT',	                    #增大B模式增益	client.simple_event('B_LEFT')
                    'b_right':'B_RIGHT',	                #减小B模式增益	client.simple_event('B_RIGHT')
                    'thi':'THI',	                        #开启/关闭谐波成像	client.simple_event('THI')
                    # CFM模式
                    'c':'CFM',
                    'c_left': 'CFM_LEFT',                   # 增大CFM增益	client.simple_event('CFM_LEFT')
                    'c_right': 'CFM_RIGHT',                 # 减小CFM增益	client.simple_event('CFM_RIGHT')
                    'cfm':'CFM',	                        #开启/关闭CFM模式	client.simple_event("CFM")
                    'cfm_left':'CFM_LEFT',	                #增大CFM增益	client.simple_event('CFM_LEFT')
                    'cfm_right':'CFM_RIGHT',	            #减小CFM增益	client.simple_event('CFM_RIGHT')
                    # PDI模式
                    'pdi':'PDI',	                        #开启/关闭PDI模式	client.simple_event("PDI")
                    # TDI模式
                    'tdi':'TDI',	                        #开启/关闭TDI模式	client.simple_event("TDI")
                    # M模式
                    'm':'M',	                            #开启/关闭M模式	client.simple_event("M")
                    'm_left':'M_LEFT',	                    #增大M增益	client.simple_event('M_LEFT')
                    'm_right':'M_RIGHT',	                #减小M增益	client.simple_event('M_RIGHT')
                    # PW模式
                    'pw':'PW',	                            #开启/关闭PW模式	client.simple_event("PW")
                    'pw_left':'PW_LEFT',	                #增大PW增益	client.simple_event('PW_LEFT')
                    'pw_right':'PW_RIGHT',	                #减小PW增益	client.simple_event('PW_RIGHT')
                    # CW模式
                    'cw':'CW',	                            #开启/关闭CW模式	client.simple_event("CW")
                    'cw_left':'CW_LEFT',	                #增大CW增益	client.simple_event('CW_LEFT')
                    'cw_right':'CW_RIGHT',	                #减小CW增益	client.simple_event('CW_RIGHT')
                    # BIOPSY
                    'biopsy':'BIOPSY',	                    #开启/关闭穿刺功能	client.simple_event('BIOPSY')
                    # ELASTO
                    'elasto':'ELASTO',	                    #开启/关闭弹性成像	client.simple_event('ELASTO')
                    # PAN
                    'pan':'PAN',	                        #开启/关闭宽景成像模式	client.simple_event('PAN')
                    # CONTRAST
                    'contrast':'CONTRAST',	                #开启造影模式	client.simple_event('CONTRAST')
                    # 3D4D
                    '3d':'3D',	                            #开启/关闭3D4D模式	client.simple_event('3D')
                    '3d4d':'3D4D',
                    'setup': 'SETUP',}

ts_button_dict = {'s-fetus(meas.)': 'NT_AI_SCALC',                  # 产科
                  's-fetus(acq.)':'NT_AI_SVIEW',
                  's-endo.':'AI_SENDO',                             # 子宫内膜
                  's-follice(r)':'AI_SFOLLICLE_RIGHT',              # 卵泡
                  's-follice(l)':'AI_SFOLLICLE_LEFT',
                  's-pf-rest(2d)':'AI_PELVIC_REST2D',                               # 二维盆底
                  's-pf-val.(2d)':'AI_PELVIC_VALSALVA2D',
                  's-pf-rest(3d)': 'B_AUTO_PF_REST',
                  's-pf-val.(3d)': 'B_AUTO_PF_VALSALVA',
                  's-pf-con.(3d)': 'B_AUTO_PF_CONTRACT',
                  '3dfz_label_ai_pf':'3DFZ_LABEL_AI_PF',
                  'auto-pf-rest(meas.)': '3DFZ_AI_PF_CON_MEA',      # 三维盆底
                  'auto-pf-rest(acq.)': '3DFZ_AI_PF_CONTRACT',
                  'auto-pf-val.(meas.)':'3DFZ_AI_PF_CON_MEA',
                  'auto-pf-val.(acq.)':'3DFZ_AI_PF_CONTRACT',
                  'auto-pf-con.(meas.)':'3DFZ_AI_PF_CON_MEA',
                  'auto-pf-con.(acq.)':'3DFZ_AI_PF_CONTRACT',
                  's-msk': 'S_MSK',                                 # 肌骨
                  'l-shoulder':'LEFT_SHOULDER',
                  'r-shoulder':'RIGHT_SHOULDER',
                  'ts-menu-page' :'TS_MENU_PAGE ',
                  'b-short':'MSK_VIEW_BICEPS_LONGUS_TENDON_SHORT',
                  'b-long' :'MSK_VIEW_BICEPS_LONGUS_TENDON_LONG ',
                  'sub-long' :'MSK_VIEW_SUBSCAPULARIS_LONG ',
                  'sub-short' :'MSK_VIEW_SUBSCAPULARIS_SHORT ',
                  'sup-long' :'MSK_VIEW_SUPRASPINATUS_LONG ',
                  'sup-short' :'MSK_VIEW_SUPRASPINATUS_SHORT ',
                  'inf-long' :'MSK_VIEW_INFRASPINATUS ',
                  'tm-long' :'MSK_VIEW_TERES_MINOR_LONG ',
                  'pgl' :'MSK_VIEW_POST_GLENOID_LABRUM ',
                  'acj' :'MSK_VIEW_ACROMIOCLAVICULAR_JOINT ',
                  'cal' :'MSK_VIEW_CORACOID_LIGAMENT ',
                  's1r': 'MSK_VIEW_BICEPS_LONGUS_TENDON_SHORT',
                  's2r': 'MSK_VIEW_BICEPS_LONGUS_TENDON_LONG ',
                  's3r': 'MSK_VIEW_SUBSCAPULARIS_LONG ',
                  's4r': 'MSK_VIEW_SUBSCAPULARIS_SHORT ',
                  's5r': 'MSK_VIEW_SUPRASPINATUS_LONG ',
                  's6r': 'MSK_VIEW_SUPRASPINATUS_SHORT ',
                  's7r': 'MSK_VIEW_INFRASPINATUS ',
                  's8r': 'MSK_VIEW_TERES_MINOR_LONG ',
                  's9r': 'MSK_VIEW_POST_GLENOID_LABRUM ',
                  's10r': 'MSK_VIEW_ACROMIOCLAVICULAR_JOINT ',
                  's11r': 'MSK_VIEW_CORACOID_LIGAMENT ',
                  'pre-view' :'MSK_PRE_VIEW ',
                  'next-view' :'MSK_NEXT_VIEW ',
                  's-msk(acq.)': 'AI_SMSK',
                  's-msk(annot.)': 'AI_AANNOT',
                  's-thyroid': 'AI_STHYROID',                       # 甲状腺
                  'trace_hr':'PWPARAM_TRACE_HR',
                  'shortcut1_left':'SHORTCUT1_LEFT',
                  'shortcut1_right':'SHORTCUT1_RIGHT',
                  'shortcut2_left': 'SHORTCUT1_LEFT',
                  'shortcut2_right': 'SHORTCUT1_RIGHT',
                  'shortcut3_left': 'SHORTCUT1_LEFT',
                  'shortcut3_right': 'SHORTCUT1_RIGHT',
                  'shortcut4_left': 'SHORTCUT1_LEFT',
                  'shortcut4_right': 'SHORTCUT1_RIGHT',
                  'shortcut5_left': 'SHORTCUT1_LEFT',
                  'shortcut5_right': 'SHORTCUT1_RIGHT',
                  }

ts_param_dict = {
                    # 通用按键
                    'exit':'EXIT',			#退出	client.adjust_param('EXIT')
                    # B模式
                    'b_frequency_up':'B_FREQUENCY_UP',			#增大B模式频率	client.adjust_param('B_FREQUENCY_UP')
                    'b_frequency_down':'B_FREQUENCY_DOWN',			#减小B模式频率	client.adjust_param('B_FREQUENCY_DOWN')
                    'b_line_density_up':'B_LINE_DENSITY_UP',			#增大B模式线密度	client.adjust_param('B_LINE_DENSITY_UP')
                    'b_line_density_down':'B_LINE_DENSITY_DOWN',			#减小B模式线密度	client.adjust_param('B_LINE_DENSITY_DOWN')
                    'b_smooth_up':'B_SMOOTH_UP',			#增大B模式平滑值	client.adjust_param('B_SMOOTH_UP')
                    'b_smooth_down':'B_SMOOTH_DOWN',			#减小B模式平滑值	client.adjust_param('B_SMOOTH_DOWN')
                    'b_sector_width_up':'B_SECTOR_WIDTH_UP',			#调节B图像面积变宽	client.adjust_param('B_SECTOR_WIDTH_UP')
                    'b_sector_width_down':'B_SECTOR_WIDTH_DOWN',			#调节B图像面积变窄	client.adjust_param('B_SECTOR_WIDTH_DOWN')
                    'b_focus_up':'B_FOCUS_UP',			#调节B图像焦点位置向深部移动	client.adjust_param('B_FOCUS_UP')
                    'b_focus_down':'B_FOCUS_DOWN',			#调节B图像焦点位置向浅部移动	client.adjust_param('B_FOCUS_DOWN')
                    'b_dyn_up':'B_DYN_UP',			#增大B图像动态范围	client.adjust_param('B_DYN_UP')
                    'b_dyn_down':'B_DYN_DOWN',			#减小B图像动态范围	client.adjust_param('B_DYN_DOWN')
                    'b_chroma_up':'B_CHROMA_UP',			#增大B图像伪彩	client.adjust_param('B_CHROMA_UP')
                    'b_chroma_down':'B_CHROMA_DOWN',			#减小B图像伪彩	client.adjust_param('B_CHROMA_DOWN')
                    'b_uscan_up':'B_USCAN_UP',			#增大微米成像值	client.adjust_param('B_USCAN_UP')
                    'b_uscan_down':'B_USCAN_DOWN',			#减小微米成像值	client.adjust_param('B_USCAN_DOWN')
                    'b_persist_up':'B_PERSIST_UP',			#增大B模式帧相关值	client.adjust_param('B_PERSIST_UP')
                    'b_persist_down':'B_PERSIST_DOWN',			#减小B模式帧相关值	client.adjust_param('B_PERSIST_DOWN')
                    'b_graymap_up':'B_GRAYMAP_UP',			#增大灰阶值	client.adjust_param('B_GRAYMAP_UP')
                    'b_graymap_down':'B_GRAYMAP_DOWN',			#减小灰阶值	client.adjust_param('B_GRAYMAP_DOWN')
                    'b_steer_up':'B_STEER_UP',			#增大B模式角度偏转	client.adjust_param('B_STEER_UP')
                    'b_steer_down':'B_STEER_DOWN',			#减小B模式角度偏转	client.adjust_param('B_STEER_DOWN')
                    'b_power_up':'B_POWER_UP',			#增大B模式输出功率值	client.adjust_param('B_POWER_UP')
                    'b_power_down':'B_POWER_DOWN',			#减小B模式输出功率值	client.adjust_param('B_POWER_DOWN')
                    'lr':'LR',			#左右翻转B图像	client.adjust_param('LR')
                    'ud':'UD',			#上下翻转B图像	client.adjust_param('UD')
                    'b_rotation':'B_ROTATION',			#调节B模式旋转角度	client.adjust_param('B_ROTATION')
                    'b_compound':'B_COMPOUND',			#开启或关闭复合成像	client.adjust_param('B_COMPOUND')
                    'b_widescan':'B_WIDESCAN',			#开启/关闭梯形成像	client.adjust_param('B_WIDESCAN')
                    'lgc':'LGC',			#开启关闭LGC功能	client.adjust_param('LGC')
                    'lgc_reset':'LGC_RESET',			#重置LGC值	client.adjust_param('LGC_RESET')
                    'lgc_exit':'LGC_EXIT',			#关闭LGC功能	client.adjust_param('LGC_EXIT')
                    'playback_f_by_f_up':'PLAYBACK_F_BY_F_UP',			#增大B图像帧值	client.adjust_param('PLAYBACK_F_BY_F_UP')
                    'playback_f_by_f_down':'PLAYBACK_F_BY_F_DOWN',			#减小B图像帧值	client.adjust_param('PLAYBACK_F_BY_F_DOWN')
                    'playback_cine_speed_up':'PLAYBACK_CINE_SPEED_UP',			#增大B图像播放速度	client.adjust_param('PLAYBACK_CINE_SPEED_UP')
                    'playback_cine_speed_down':'PLAYBACK_CINE_SPEED_DOWN',			#减小B图像播放速度	client.adjust_param('PLAYBACK_CINE_SPEED_DOWN')
                    'playback_set_firstframe_up':'PLAYBACK_SET_FIRSTFRAME_UP',			#增大B图像首帧位置	client.adjust_param('PLAYBACK_SET_FIRSTFRAME_UP')
                    'playback_set_firstframe_down':'PLAYBACK_SET_FIRSTFRAME_DOWN',			#减小B图像首帧位置	client.adjust_param('PLAYBACK_SET_FIRSTFRAME_DOWN')
                    'playback_set_lastframe_up':'PLAYBACK_SET_LASTFRAME_UP',			#增大B图像尾帧位置	client.adjust_param('PLAYBACK_SET_LASTFRAME_UP')
                    'playback_set_lastframe_down':'PLAYBACK_SET_LASTFRAME_DOWN',			#减小B图像尾帧位置	client.adjust_param('PLAYBACK_SET_LASTFRAME_DOWN')
                    'playback_to_first':'PLAYBACK_TO_FIRST',			#回放到B图像首帧	client.adjust_param('PLAYBACK_TO_FIRST')
                    'playback_to_last':'PLAYBACK_TO_LAST',			#回放到B图像尾帧	client.adjust_param('PLAYBACK_TO_LAST')
                    'playback_auto_play':'PLAYBACK_AUTO_PLAY',			#自动回放B图像	client.adjust_param('PLAYBACK_AUTO_PLAY')
                    # CFM模式
                    'c_pdi_tdi_frequency_up':'C/PDI/TDI_FREQUENCY_UP',			#增大CFM频率	client.adjust_param('C/PDI/TDI_FREQUENCY_UP')
                    'c_pdi_tdi_frequency_down':'C/PDI/TDI_FREQUENCY_DOWN',			#减小CFM频率	client.adjust_param('C/PDI/TDI_FREQUENCY_DOWN')
                    'c_pdi_tdi_line_density_up':'C/PDI/TDI_LINE_DENSITY_UP',			#增大CFM线密度	client.adjust_param('C/PDI/TDI_LINE_DENSITY_UP')
                    'c_pdi_tdi_line_density_down':'C/PDI/TDI_LINE_DENSITY_DOWN',			#减小CFM线密度	client.adjust_param('C/PDI/TDI_LINE_DENSITY_DOWN')
                    'c_pdi_tdi_wf_up':'C/PDI/TDI_WF_UP',			#增大CFM的壁滤波值	client.adjust_param('C/PDI/TDI_WF_UP')
                    'c_pdi_tdi_wf_down':'C/PDI/TDI_WF_DOWN',			#减小CFM的壁滤波值	client.adjust_param('C/PDI/TDI_WF_DOWN')
                    'c_pdi_tdi_b_reject_up':'C/PDI/TDI_B_REJECT_UP',			#增大B抑制	client.adjust_param('C/PDI/TDI_B_REJECT_UP')
                    'c_pdi_tdi_b_reject_down':'C/PDI/TDI_B_REJECT_DOWN',			#减小B抑制	client.adjust_param('C/PDI/TDI_B_REJECT_DOWN')
                    'c_pdi_tdi_power_up':'C/PDI/TDI_POWER_UP',			#增大CFM功率	client.adjust_param('C/PDI/TDI_POWER_UP')
                    'c_pdi_tdi_power_down':'C/PDI/TDI_POWER_DOWN',			#减小CFM功率	client.adjust_param('C/PDI/TDI_POWER_DOWN')
                    'c_pdi_tdi_dual_live':'C/PDI/TDI_DUAL_LIVE',			#开启/关闭双幅实时显示	client.adjust_param('C/PDI/TDI_DUAL_LIVE')
                    'c_tdi_invert':'C/TDI_INVERT',			#开启/关闭血流反转	client.adjust_param('C/TDI_INVERT')
                    'c_tdi_persist_up':'C/TDI_PERSIST_UP',			#增大CFM的帧相关值	client.adjust_param('C/TDI_PERSIST_UP')
                    'c_tdi_persist_down':'C/TDI_PERSIST_DOWN',			#减小CFM的帧相关值	client.adjust_param('C/TDI_PERSIST_DOWN')
                    'cfm_steer_up':'CFM_STEER_UP',			#增大CFM的角度偏转	client.adjust_param('CFM_STEER_UP')
                    'cfm_steer_down':'CFM_STEER_DOWN',			#减小CFM的角度偏转	client.adjust_param('CFM_STEER_DOWN')
                    'cfm_smooth_up':'CFM_SMOOTH_UP',			#增大CFM的平滑值	client.adjust_param('CFM_SMOOTH_UP')
                    'cfm_smooth_down':'CFM_SMOOTH_DOWN',			#减小CFM的平滑值	client.adjust_param('CFM_SMOOTH_DOWN')
                    'cfm_cmap_up':'CFM_CMAP_UP',			#增大CFM彩色图谱值	client.adjust_param('CFM_CMAP_UP')
                    'cfm_cmap_down':'CFM_CMAP_DOWN',			#减小CFM彩色图谱值	client.adjust_param('CFM_CMAP_DOWN')
                    'cfm_freeze_hide_flow':'CFM_FREEZE_HIDE_FLOW',			#冻结时开启隐藏血流功能	client.adjust_param('CFM_FREEZE_HIDE_FLOW')
                    # PDI模式
                    'pdi_persist_up':'PDI_PERSIST_UP',			#增大PDI的帧相关值	client.adjust_param('PDI_PERSIST_UP')
                    'pdi_persist_down':'PDI_PERSIST_DOWN',			#减小PDI的帧相关值	client.adjust_param('PDI_PERSIST_DOWN')
                    'pdi_map_dpdi_up':'PDI_MAP/DPDI_UP',			#增大彩色图谱值	client.adjust_param('PDI_MAP/DPDI_UP')
                    'pdi_map_dpdi_down':'PDI_MAP/DPDI_DOWN',			#减小彩色图谱值	client.adjust_param('PDI_MAP/DPDI_DOWN')
                    'dpdi_hd_flow_switch':'DPDI_HD_FLOW_SWITCH',			#开启/关闭高分辨率血流功能	client.adjust_param('DPDI_HD_FLOW_SWITCH')
                    'pdi_srf':'DPDI_HD_FLOW_SWITCH',			#开启/关闭高分辨率血流功能	client.adjust_param('DPDI_HD_FLOW_SWITCH')
                    # TDI模式
                    'tdi_cmap_up':'TDI_CMAP_UP',			#增大彩色图谱值	client.adjust_param('TDI_CMAP_UP')
                    'tdi_cmap_down':'TDI_CMAP_DOWN',			#减小彩色图谱值	client.adjust_param('TDI_CMAP_DOWN')
                    'tdi_tic':'TDI_TIC',			#开启/关闭Wallmotion功能	client.adjust_param('TDI_TIC')
                    'tic_trace_delete_all':'TIC_TRACE_DELETE_ALL',			#清除Wallmotion	client.adjust_param('TIC_TRACE_DELETE_ALL')
                    'tic_trace_finish':'TIC_TRACE_FINISH',			#完成Wallmotion	client.adjust_param('TIC_TRACE_FINISH')
                    'tic_view_type':'TIC_VIEW_TYPE',			#分段显示Wallmotion	client.adjust_param('TIC_VIEW_TYPE')
                    'tic_data_type_down':'TIC_DATA_TYPE_DOWN',			#向左调弹性曲线	client.adjust_param('TIC_DATA_TYPE_DOWN')
                    'tic_data_type_up':'TIC_DATA_TYPE_UP',			#向右调弹性曲线	client.adjust_param('TIC_DATA_TYPE_UP')
                    # M模式
                    'm_chroma_up':'M_CHROMA_UP',			#增大M图像伪彩	client.adjust_param('M_CHROMA_UP')
                    'm_chroma_down':'M_CHROMA_DOWN',			#减小M图像伪彩	client.adjust_param('M_CHROMA_DOWN')
                    'm_graymap_up':'M_GRAYMAP_UP',			#增大灰阶值	client.adjust_param('M_GRAYMAP_UP')
                    'm_graymap_down':'M_GRAYMAP_DOWN',			#减小灰阶值	client.adjust_param('M_GRAYMAP_DOWN')
                    'm_power_down':'M_POWER_DOWN',			#增大M功率	client.adjust_param('M_POWER_DOWN')
                    'm_power_up':'M_POWER_UP',			#减小M功率	client.adjust_param('M_POWER_UP')
                    'm_video_invert':'M_VIDEO_INVERT',			#开启/关闭视频反转	client.adjust_param('M_VIDEO_INVERT')
                    'm_mprocess_up':'M_MPROCESS_UP',			#更改M型处理为峰值	client.adjust_param('M_MPROCESS_UP')
                    'm_mprocess_down':'M_MPROCESS_DOWN',			#更改M型处理为平均	client.adjust_param('M_MPROCESS_DOWN')
                    'm_display_up':'M_DISPLAY_UP',			#向右调节M显示格式	client.adjust_param('M_DISPLAY_UP')
                    'm_display_down':'M_DISPLAY_DOWN',			#向左调节M显示格式	client.adjust_param('M_DISPLAY_DOWN')
                    'm_speed_up':'M_SPEED_UP',			#增大扫描速度	client.adjust_param('M_SPEED_UP')
                    'm_speed_down':'M_SPEED_DOWN',			#减小扫描速度	client.adjust_param('M_SPEED_DOWN')
                    'm_smooth_up':'M_SMOOTH_UP',			#增大M模式的平滑值	client.adjust_param('M_SMOOTH_UP')
                    'm_smooth_down':'M_SMOOTH_DOWN',			#减小M模式的平滑值	client.adjust_param('M_SMOOTH_DOWN')
                    'amm_switch_level':'AMM_SWITCH_LEVEL',			#开启/关闭解剖M模式	client.adjust_param('AMM_SWITCH_LEVEL')
                    'amm_chroma_up':'AMM_CHROMA_UP',			#增大解剖M图像伪彩	client.adjust_param('AMM_CHROMA_UP')
                    'amm_chroma_down':'AMM_CHROMA_DOWN',			#减小解剖M图像伪彩	client.adjust_param('AMM_CHROMA_DOWN')
                    'amm_line_num_level_up':'AMM_LINE_NUM_LEVEL_UP',			#增大AMM样线个数	client.adjust_param('AMM_LINE_NUM_LEVEL_UP')
                    'amm_line_num_level_down':'AMM_LINE_NUM_LEVEL_DOWN',			#减小AMM样线个数	client.adjust_param('AMM_LINE_NUM_LEVEL_DOWN')
                    'amm_angle_level_up':'AMM_ANGLE_LEVEL_UP',			#增大AMM取样线角度	client.adjust_param('AMM_ANGLE_LEVEL_UP')
                    'amm_angle_level_down':'AMM_ANGLE_LEVEL_DOWN',			#减小AMM取样线角度	client.adjust_param('AMM_ANGLE_LEVEL_DOWN')
                    'amm_sweep_speed_up':'AMM_SWEEP_SPEED_UP',			#增大AMM扫描速度	client.adjust_param('AMM_SWEEP_SPEED_UP')
                    'amm_sweep_speed_down':'AMM_SWEEP_SPEED_DOWN',			#减小AMM扫描速度	client.adjust_param('AMM_SWEEP_SPEED_DOWN')
                    'amm_video_invert':'AMM_VIDEO_INVERT',			#开启/关闭视频反转	client.adjust_param('AMM_VIDEO_INVERT')
                    'amm_mprocess_up':'AMM_MPROCESS_UP',			#更改M型处理为峰值	client.adjust_param('AMM_MPROCESS_UP')
                    'amm_mprocess_down':'AMM_MPROCESS_DOWN',			#更改M型处理为平均	client.adjust_param('AMM_MPROCESS_DOWN')
                    # PW模式
                    'pw_frequency_up':'PW_FREQUENCY_UP',			#增大PW频率	client.adjust_param('PW_FREQUENCY_UP')
                    'pw_frequency_down':'PW_FREQUENCY_DOWN',			#减小PW频率	client.adjust_param('PW_FREQUENCY_DOWN')
                    'pw_dyn_up':'PW_DYN_UP',			#增大PW动态范围	client.adjust_param('PW_DYN_UP')
                    'pw_dyn_down':'PW_DYN_DOWN',			#减小PW动态范围	client.adjust_param('PW_DYN_DOWN')
                    'pw_chroma_up':'PW_CHROMA_UP',			#增大PW图像伪彩	client.adjust_param('PW_CHROMA_UP')
                    'pw_chroma_down':'PW_CHROMA_DOWN',			#减小PW图像伪彩	client.adjust_param('PW_CHROMA_DOWN')
                    'pw_power_up':'PW_POWER_UP',			#增大PW功率	client.adjust_param('PW_POWER_UP')
                    'pw_power_down':'PW_POWER_DOWN',			#减小PW功率	client.adjust_param('PW_POWER_DOWN')
                    'pw_steerlevel_up':'PW_STEERLEVEL_UP',			#增大PW角度偏转	client.adjust_param('PW_STEERLEVEL_UP')
                    'pw_steerlevel_down':'PW_STEERLEVEL_DOWN',			#减小PW角度偏转	client.adjust_param('PW_STEERLEVEL_DOWN')
                    'pw_invert':'PW_INVERT',			#开启/关闭PW反转	client.adjust_param('PW_INVERT')
                    'pw_smooth_up':'PW_SMOOTH_UP',			#增大PW模式的平滑值	client.adjust_param('PW_SMOOTH_UP')
                    'pw_smooth_down':'PW_SMOOTH_DOWN',			#减小PW模式的平滑值	client.adjust_param('PW_SMOOTH_DOWN')
                    'pw_wf_up':'PW_WF_UP',			#增大PW模式的壁滤波值	client.adjust_param('PW_WF_UP')
                    'pw_wf_down':'PW_WF_DOWN',			#减小PW模式的壁滤波值	client.adjust_param('PW_WF_DOWN')
                    'pw_display_up':'PW_DISPLAY_UP',			#向右调节PW显示格式	client.adjust_param('PW_DISPLAY_UP')
                    'pw_display_down':'PW_DISPLAY_DOWN',			#向左调节PW显示格式	client.adjust_param('PW_DISPLAY_DOWN')
                    'pw_speed_up':'PW_SPEED_UP',			#增大PW扫描速度	client.adjust_param('PW_SPEED_UP')
                    'pw_speed_down':'PW_SPEED_DOWN',			#减小PW扫描速度	client.adjust_param('PW_SPEED_DOWN')
                    'pw_nsi_up':'PW_NSI_UP',			#增大PW模式的噪声抑制	client.adjust_param('PW_NSI_UP')
                    'pw_nsi_down':'PW_NSI_DOWN',			#减小PW模式的噪声抑制	client.adjust_param('PW_NSI_DOWN')
                    'pw_audio_up':'PW_AUDIO_UP',			#增大PW的音量	client.adjust_param('PW_AUDIO_UP')
                    'pw_audio_down':'PW_AUDIO_DOWN',			#减小PW的音量	client.adjust_param('PW_AUDIO_DOWN')
                    'pw_autotrace':'PW_AUTOTRACE',			#开启/关闭PW自动描迹功能	client.adjust_param('PW_AUTOTRACE')
                    'autotrace':'PW_AUTOTRACE',			#开启/关闭PW自动描迹功能	client.adjust_param('PW_AUTOTRACE')
                    'pw_simult':'PW_SIMULT',			#开启/关闭PW双同步模式	client.adjust_param('PW_SIMULT')
                    # CW模式
                    'cw_frequency_up':'CW_FREQUENCY_UP',			#增大CW频率	client.adjust_param('CW_FREQUENCY_UP')
                    'cw_frequency_down':'CW_FREQUENCY_DOWN',			#减小CW频率	client.adjust_param('CW_FREQUENCY_DOWN')
                    'cw_dyn_up':'CW_DYN_UP',			#增大CW动态范围	client.adjust_param('CW_DYN_UP')
                    'cw_dyn_down':'CW_DYN_DOWN',			#减小CW动态范围	client.adjust_param('CW_DYN_DOWN')
                    'cw_chroma_up':'CW_CHROMA_UP',			#增大CW图像伪彩	client.adjust_param('CW_CHROMA_UP')
                    'cw_chroma_down':'CW_CHROMA_DOWN',			#减小CW图像伪彩	client.adjust_param('CW_CHROMA_DOWN')
                    'cw_power_up':'CW_POWER_UP',			#增大CW功率	client.adjust_param('CW_POWER_UP')
                    'cw_power_down':'CW_POWER_DOWN',			#减小CW功率	client.adjust_param('CW_POWER_DOWN')
                    'cw_invert':'CW_INVERT',			#开启/关闭CW反转	client.adjust_param('CW_INVERT')
                    'cw_smooth_up':'CW_SMOOTH_UP',			#增大CW模式的平滑值	client.adjust_param('CW_SMOOTH_UP')
                    'cw_smooth_down':'CW_SMOOTH_DOWN',			#减小CW模式的平滑值	client.adjust_param('CW_SMOOTH_DOWN')
                    'cw_wf_up':'CW_WF_UP',			#增大CW模式的壁滤波值	client.adjust_param('CW_WF_UP')
                    'cw_wf_down':'CW_WF_DOWN',			#减小CW模式的壁滤波值	client.adjust_param('CW_WF_DOWN')
                    'cw_display_up':'CW_DISPLAY_UP',			#向右调节CW显示格式	client.adjust_param('CW_DISPLAY_UP')
                    'cw_display_down':'CW_DISPLAY_DOWN',			#向左调节CW显示格式	client.adjust_param('CW_DISPLAY_DOWN')
                    'cw_speed_up':'CW_SPEED_UP',			#增大CW扫描速度	client.adjust_param('CW_SPEED_UP')
                    'cw_speed_down':'CW_SPEED_DOWN',			#减小CW扫描速度	client.adjust_param('CW_SPEED_DOWN')
                    'cw_nsi_up':'CW_NSI_UP',			#增大CW模式的噪声抑制	client.adjust_param('CW_NSI_UP')
                    'cw_nsi_down':'CW_NSI_DOWN',			#减小CW模式的噪声抑制	client.adjust_param('CW_NSI_DOWN')
                    'cw_audio_up':'CW_AUDIO_UP',			#增大CW的音量	client.adjust_param('CW_AUDIO_UP')
                    'cw_audio_down':'CW_AUDIO_DOWN',			#减小CW的音量	client.adjust_param('CW_AUDIO_DOWN')
                    'cw_autotrace':'CW_AUTOTRACE',			#开启/关闭CW自动描迹功能	client.adjust_param('CW_AUTOTRACE')
                    # BIOPSY
                    'biopsy_level_up':'BIOPSY_LEVEL_UP',			#增大穿刺值/增大穿刺矫正角度	client.adjust_param('BIOPSY_LEVEL_UP')
                    'biopsy_level_down':'BIOPSY_LEVEL_DOWN',			#减小穿刺值/减小穿刺矫正角度	client.adjust_param('BIOPSY_LEVEL_DOWN')
                    'biopsy_dotsize_up':'BIOPSY_DOTSIZE_UP',			#增大点大小	client.adjust_param('BIOPSY_DOTSIZE_UP')
                    'biopsy_dotsize_down':'BIOPSY_DOTSIZE_DOWN',			#减小点大小	client.adjust_param('BIOPSY_DOTSIZE_DOWN')
                    'biopsy_cali':'BIOPSY_CALI',			#开启穿刺矫正	client.adjust_param('BIOPSY_CALI')
                    'biopsy_angle_up':'BIOPSY_ANGLE_UP',			#增大穿刺角度	client.adjust_param('BIOPSY_ANGLE_UP')
                    'biopsy_angle_down':'BIOPSY_ANGLE_DOWN',			#减小穿刺角度	client.adjust_param('BIOPSY_ANGLE_DOWN')
                    'biopsy_offset_up':'BIOPSY_OFFSET_UP',			#增大穿刺偏移	client.adjust_param('BIOPSY_OFFSET_UP')
                    'biopsy_offset_down':'BIOPSY_OFFSET_DOWN',			#减小穿刺偏移	client.adjust_param('BIOPSY_OFFSET_DOWN')
                    # VIS-NEEDLE
                    'biopsy_visneedle_level_up':'BIOPSY_VISNEEDLE_LEVEL_UP',			#开启/关闭穿刺增强	client.adjust_param('BIOPSY_VISNEEDLE_LEVEL_UP')
                    'biopsy_steerangle_level_up':'BIOPSY_STEERANGLE_LEVEL_UP',			#增大偏转角度	client.adjust_param('BIOPSY_STEERANGLE_LEVEL_UP')
                    'biopsy_steerangle_level_down':'BIOPSY_STEERANGLE_LEVEL_DOWN',			#减小偏转角度	client.adjust_param('BIOPSY_STEERANGLE_LEVEL_DOWN')
                    'biopsy_duallive':'BIOPSY_DUALLIVE',			#双幅实时显示	client.adjust_param('BIOPSY_DUALLIVE')
                    # ELASTO
                    'elastro_frequency_up':'ELASTRO_FREQUENCY_UP',			#增大ELASTO频率	client.adjust_param('ELASTRO_FREQUENCY_UP')
                    'elastro_frequency_down':'ELASTRO_FREQUENCY_DOWN',			#减小ELASTO频率	client.adjust_param('ELASTRO_FREQUENCY_DOWN')
                    'elastro_strain_proce_up':'ELASTRO_STRAIN_PROCE_UP',			#增大弹性处理值	client.adjust_param('ELASTRO_STRAIN_PROCE_UP')
                    'elastro_strain_proce_down':'ELASTRO_STRAIN_PROCE_DOWN',			#减小弹性处理值	client.adjust_param('ELASTRO_STRAIN_PROCE_DOWN')
                    'elastro_strain_map_l_up':'ELASTRO_STRAIN_MAP_L_UP',			#增大左幅图谱颜色值	client.adjust_param('ELASTRO_STRAIN_MAP_L_UP')
                    'elastro_strain_map_l_down':'ELASTRO_STRAIN_MAP_L_DOWN',			#减小左幅图谱颜色值	client.adjust_param('ELASTRO_STRAIN_MAP_L_DOWN')
                    'elastro_strain_map_r_up':'ELASTRO_STRAIN_MAP_R_UP',			#加入/ 增大右幅图谱颜色值	client.adjust_param('ELASTRO_STRAIN_MAP_R_UP')
                    'elastro_strain_map_r_down':'ELASTRO_STRAIN_MAP_R_DOWN',			#去掉/减小右幅图谱颜色值	client.adjust_param('ELASTRO_STRAIN_MAP_R_DOWN')
                    'elastro_contrast_up':'ELASTRO_CONTRAST_UP',			#增大ELASTO软硬度色彩的对比度	client.adjust_param('ELASTRO_CONTRAST_UP')
                    'elastro_contrast_down':'ELASTRO_CONTRAST_DOWN',			#减小ELASTO软硬度色彩的对比度	client.adjust_param('ELASTRO_CONTRAST_DOWN')
                    'elastro_transparency_up':'ELASTRO_TRANSPARENCY_UP',			#增大ELASTO透明度	client.adjust_param('ELASTRO_TRANSPARENCY_UP')
                    'elastro_transparency_down':'ELASTRO_TRANSPARENCY_DOWN',			#减小ELASTO透明度	client.adjust_param('ELASTRO_TRANSPARENCY_DOWN')
                    'elastro_persist_up':'ELASTRO_PERSIST_UP',			#增大ELASTO帧相关值	client.adjust_param('ELASTRO_PERSIST_UP')
                    'elastro_persist_down':'ELASTRO_PERSIST_DOWN',			#减小ELASTO帧相关值	client.adjust_param('ELASTRO_PERSIST_DOWN')
                    # PAN
                    'pan_start':'PAN_START',			#开始采集图像	client.adjust_param('PAN_START')
                    'pan_stop':'PAN_STOP',			#停止采集图像	client.adjust_param('PAN_STOP')
                    'pan_zoom_up':'PAN_ZOOM_UP',			#放大图像	client.adjust_param('PAN_ZOOM_UP')
                    'pan_zoom_down':'PAN_ZOOM_DOWN',			#缩小图像	client.adjust_param('PAN_ZOOM_DOWN')
                    'pan_rotate_up':'PAN_ROTATE_UP',			#增大旋转角度	client.adjust_param('PAN_ROTATE_UP')
                    'pan_rotate_down':'PAN_ROTATE_DOWN',			#减小旋转角度	client.adjust_param('PAN_ROTATE_DOWN')
                    'pan_overview':'PAN_OVERVIEW',			#全视图，将缩放或旋转后的图像恢复到原始状态	client.adjust_param('PAN_OVERVIEW')
                    'pan_ruler':'PAN_RULER',			#对图像进行测量、体位标记和注释等操作	client.adjust_param('PAN_RULER')
                    'pan_recapture':'PAN_RECAPTURE',			#重新采集图像	client.adjust_param('PAN_RECAPTURE')
                    # CONTRAST
                    'contrast_timer1':'CONTRAST_TIMER1',			#开启/关闭计时器1	client.adjust_param('CONTRAST_TIMER1')
                    'contrast_timer2':'CONTRAST_TIMER2',			#开启/关闭计时器2	client.adjust_param('CONTRAST_TIMER2')
                    'cine_real_future':'CINE_REAL_FUTURE',			#向后存储	client.adjust_param('CINE_REAL_FUTURE')
                    'cine_real_forward':'CINE_REAL_FORWARD',			#向前存储	client.adjust_param('CINE_REAL_FORWARD')
                    'contrast_image':'CONTRAST_IMAGE',			#左右切换造影图像	client.adjust_param('CONTRAST_IMAGE')
                    'contrast_ld_up':'CONTRAST_LD_UP',			#增大contrast线密度	client.adjust_param('CONTRAST_LD_UP')
                    'contrast_ld_down':'CONTRAST_LD_DOWN',			#减小contrast线密度	client.adjust_param('CONTRAST_LD_DOWN')
                    'contrast_flash':'CONTRAST_FLASH',			#开启爆破	client.adjust_param('CONTRAST_FLASH')
                    'single_view':'SINGLE_VIEW',			#单幅显示contrast	client.adjust_param('SINGLE_VIEW')
                    'dual':'DUAL',			#双幅显示contrast	client.adjust_param('DUAL')
                    'contrast_flashpower_up':'CONTRAST_FLASHPOWER_UP',			#增大闪烁功率	client.adjust_param('CONTRAST_FLASHPOWER_UP')
                    'contrast_flashpower_down':'CONTRAST_FLASHPOWER_DOWN',			#减小闪烁功率	client.adjust_param('CONTRAST_FLASHPOWER_DOWN')
                    'contrast_flashtimer_up':'CONTRAST_FLASHTIMER_UP',			#增大爆破时间	client.adjust_param('CONTRAST_FLASHTIMER_UP')
                    'contrast_flashtimer_down':'CONTRAST_FLASHTIMER_DOWN',			#减小爆破时间	client.adjust_param('CONTRAST_FLASHTIMER_DOWN')
                    'contrast_frequency_up':'CONTRAST_FREQUENCY_UP',			#增大Contrast频率	client.adjust_param('CONTRAST_FREQUENCY_UP')
                    'contrast_frequency_down':'CONTRAST_FREQUENCY_DOWN',			#减小Contrast频率	client.adjust_param('CONTRAST_FREQUENCY_DOWN')
                    'contrast_uscan_up':'CONTRAST_USCAN_UP',			#增大contrast微米成像值	client.adjust_param('CONTRAST_USCAN_UP')
                    'contrast_uscan_down':'CONTRAST_USCAN_DOWN',			#减小contrast微米成像值	client.adjust_param('CONTRAST_USCAN_DOWN')
                    'contrast_dynamicrange_up':'CONTRAST_DYNAMICRANGE_UP',			#增大contrast动态范围	client.adjust_param('CONTRAST_DYNAMICRANGE_UP')
                    'contrast_dynamicrange_down':'CONTRAST_DYNAMICRANGE_DOWN',			#减小contrast动态范围	client.adjust_param('CONTRAST_DYNAMICRANGE_DOWN')
                    'contrast_focus_pos_up':'CONTRAST_FOCUS_POS_UP',			#调高contrast焦点位置	client.adjust_param('CONTRAST_FOCUS_POS_UP')
                    'contrast_focus_pos_down':'CONTRAST_FOCUS_POS_DOWN',			#降低contrast焦点位置	client.adjust_param('CONTRAST_FOCUS_POS_DOWN')
                    'contrast_power_up':'CONTRAST_POWER_UP',			#增大contrast探头声输出功率值	client.adjust_param('CONTRAST_POWER_UP')
                    'contrast_power_down':'CONTRAST_POWER_DOWN',			#减小contrast探头声输出功率值	client.adjust_param('CONTRAST_POWER_DOWN')
                    'contrast_graymap_up':'CONTRAST_GRAYMAP_UP',			#增大contrast灰阶图谱值	client.adjust_param('CONTRAST_GRAYMAP_UP')
                    'contrast_graymap_down':'CONTRAST_GRAYMAP_DOWN',			#减小contrast灰阶图谱值	client.adjust_param('CONTRAST_GRAYMAP_DOWN')
                    'contrast_secwid_up':'CONTRAST_SECWID_UP',			#增大contrast扇扫宽度	client.adjust_param('CONTRAST_SECWID_UP')
                    'contrast_secwid_down':'CONTRAST_SECWID_DOWN',			#减小contrast扇扫宽度	client.adjust_param('CONTRAST_SECWID_DOWN')
                    'contrast_chroma_up':'CONTRAST_CHROMA_UP',			#增大contrast伪彩	client.adjust_param('CONTRAST_CHROMA_UP')
                    'contrast_chroma_down':'CONTRAST_CHROMA_DOWN',			#减小contrast伪彩	client.adjust_param('CONTRAST_CHROMA_DOWN')
                    'contrast_persist_up':'CONTRAST_PERSIST_UP',			#增大contrast帧相关值	client.adjust_param('CONTRAST_PERSIST_UP')
                    'contrast_persist_down':'CONTRAST_PERSIST_DOWN',			#减小contrast帧相关值	client.adjust_param('CONTRAST_PERSIST_DOWN')
                    'contrast_mfi':'CONTRAST_MFI',			#开启/关闭MFI	client.adjust_param('CONTRAST_MFI')
                    'contrast_mficyclelevel_down':'CONTRAST_MFICYCLELEVEL_DOWN',			#增大MFI CYCLE值	client.adjust_param('CONTRAST_MFICYCLELEVEL_DOWN')
                    'contrast_mficyclelevel_up':'CONTRAST_MFICYCLELEVEL_UP',			#减小MFI CYCLE值	client.adjust_param('CONTRAST_MFICYCLELEVEL_UP')
                    'contrast_mix':'CONTRAST_MIX',			#开启/关闭MIX	client.adjust_param('CONTRAST_MIX')
                    'contrast_mfi_time':'CONTRAST_MFI_TIME',			#开启/关闭MFI_TIME	client.adjust_param('CONTRAST_MFI_TIME')
                    'contrast_tic':'CONTRAST_TIC',			#开启TIC	client.adjust_param('CONTRAST_TIC')
                    'contrast_tic_curvefitt':'CONTRAST_TIC_CURVEFITT',			#开启/关闭拟合曲线	client.adjust_param('CONTRAST_TIC_CURVEFITT')
                    'contrast_tic_curvefitthide':'CONTRAST_TIC_CURVEFITTHIDE',			#隐藏拟合曲线	client.adjust_param('CONTRAST_TIC_CURVEFITTHIDE')
                    'contrast_tic_boluswiwo':'CONTRAST_TIC_BOLUSWIWO',			#快速注射	client.adjust_param('CONTRAST_TIC_BOLUSWIWO')
                    'contrast_tic_general':'CONTRAST_TIC_GENERAL',			#通用模式	client.adjust_param('CONTRAST_TIC_GENERAL')
                    'contrast_tic_washin':'CONTRAST_TIC_WASHIN',			#Wash In功能	client.adjust_param('CONTRAST_TIC_WASHIN')
                    'contrast_tic_washout':'CONTRAST_TIC_WASHOUT',			#Wash Out功能	client.adjust_param('CONTRAST_TIC_WASHOUT')
                    'contrast_tic_trace':'CONTRAST_TIC_TRACE',			#手动描迹	client.adjust_param('CONTRAST_TIC_TRACE')
                    'contrast_tic_param_display':'CONTRAST_TIC_PARAM_DISPLAY',			#参数显示	client.adjust_param('CONTRAST_TIC_PARAM_DISPLAY')
                    'contrast_tic_delete_one':'CONTRAST_TIC_DELETE_ONE',			#删除单个	client.adjust_param('CONTRAST_TIC_DELETE_ONE')
                    'contrast_tic_ellipse':'CONTRAST_TIC_ELLIPSE',			#椭圆测量	client.adjust_param('CONTRAST_TIC_ELLIPSE')
                    'contrast_tic_delete_all':'CONTRAST_TIC_DELETE_ALL',			#清除所有	client.adjust_param('CONTRAST_TIC_DELETE_ALL')
                    'ts_menu_title_1':'TS_MENU_TITLE_1',			#开启组织功能	client.adjust_param('TS_MENU_TITLE_1')
                    'tissue_frequency_up':'TISSUE_FREQUENCY_UP',			#增大组织频率	client.adjust_param('TISSUE_FREQUENCY_UP')
                    'tissue_frequency_down':'TISSUE_FREQUENCY_DOWN',			#减小组织频率	client.adjust_param('TISSUE_FREQUENCY_DOWN')
                    'tissue_dynamicrangelevel_up':'TISSUE_DYNAMICRANGELEVEL_UP',			#增大组织动态范围	client.adjust_param('TISSUE_DYNAMICRANGELEVEL_UP')
                    'tissue_dynamicrangelevel_down':'TISSUE_DYNAMICRANGELEVEL_DOWN',			#减小组织动态范围	client.adjust_param('TISSUE_DYNAMICRANGELEVEL_DOWN')
                    'tissue_powerlevel_up':'TISSUE_POWERLEVEL_UP',			#增大组织功率	client.adjust_param('TISSUE_POWERLEVEL_UP')
                    'tissue_powerlevel_down':'TISSUE_POWERLEVEL_DOWN',			#减小组织功率	client.adjust_param('TISSUE_POWERLEVEL_DOWN')
                    # ECG
                    'ecg_menu_switch':'ECG_MENU_SWITCH',			#开启/关闭ECG模块	client.adjust_param('ECG_MENU_SWITCH')
                    'ecg':'ECG',			#开启/关闭ECG曲线	client.adjust_param('ECG')
                    'ecg_invert':'ECG_INVERT',			#开启/关闭ECG曲线反转	client.adjust_param('ECG_INVERT')
                    'ecg_gain_up':'ECG_GAIN_UP',			#增大ECG增益	client.adjust_param('ECG_GAIN_UP')
                    'ecg_gain_down':'ECG_GAIN_DOWN',			#减小ECG增益	client.adjust_param('ECG_GAIN_DOWN')
                    'ecg_position_up':'ECG_POSITION_UP',			#升高ECG曲线位置	client.adjust_param('ECG_POSITION_UP')
                    'ecg_position_down':'ECG_POSITION_DOWN',			#降低ECG曲线位置	client.adjust_param('ECG_POSITION_DOWN')
                    'ecg_trigger':'ECG_TRIGGER',			#开启/关闭R波触发功能	client.adjust_param('ECG_TRIGGER')
                    'ecg_trigger_delay_up':'ECG_TRIGGER_DELAY_UP',			#增大R波触发延迟	client.adjust_param('ECG_TRIGGER_DELAY_UP')
                    'ecg_trigger_delay_down':'ECG_TRIGGER_DELAY_DOWN',			#减小R波触发延迟	client.adjust_param('ECG_TRIGGER_DELAY_DOWN')
                    'ecg_frame_count_up':'ECG_FRAME_COUNT_UP',			#增大R波频数计数	client.adjust_param('ECG_FRAME_COUNT_UP')
                    'ecg_frame_count_down':'ECG_FRAME_COUNT_DOWN',			#减小R波频数计数	client.adjust_param('ECG_FRAME_COUNT_DOWN')
                    # STRESSECHO
                    'stressecho':'STRESSECHO',			#开启负荷超声	client.adjust_param('STRESSECHO')
                    'se_protocol_1':'SE_PROTOCOL_1',			#选择Exercise 2*4	client.adjust_param('SE_PROTOCOL_1')
                    'se_protocol_2':'SE_PROTOCOL_2',			#选择协议Exercise 3*4	client.adjust_param('SE_PROTOCOL_2')
                    'se_protocol_3':'SE_PROTOCOL_3',			#选择协议Pharam 4*4	client.adjust_param('SE_PROTOCOL_3')
                    'stressecho_exam_timer':'STRESSECHO_EXAM_TIMER',			#开启/关闭检查计时	client.adjust_param('STRESSECHO_EXAM_TIMER')
                    'stressecho_stage_timer':'STRESSECHO_STAGE_TIMER',			#开启/关闭阶段计时	client.adjust_param('STRESSECHO_STAGE_TIMER')
                    'stressecho_skip_view':'STRESSECHO_SKIP_VIEW',			#跳过切面	client.adjust_param('STRESSECHO_SKIP_VIEW')
                    'stressecho_scan_view_up':'STRESSECHO_SCAN_VIEW_UP',			#向右切换切面	client.adjust_param('STRESSECHO_SCAN_VIEW_UP')
                    'stressecho_scan_view_down':'STRESSECHO_SCAN_VIEW_DOWN',			#向左切换切面	client.adjust_param('STRESSECHO_SCAN_VIEW_DOWN')
                    'stressecho_loop_length_up':'STRESSECHO_LOOP_LENGTH_UP',			#增大电影长度	client.adjust_param('STRESSECHO_LOOP_LENGTH_UP')
                    'stressecho_loop_length_down':'STRESSECHO_LOOP_LENGTH_DOWN',			#减小电影长度	client.adjust_param('STRESSECHO_LOOP_LENGTH_DOWN')
                    'stressecho_suspend':'STRESSECHO_SUSPEND',			#挂起SE	client.adjust_param('STRESSECHO_SUSPEND')
                    'stressecho_resume':'STRESSECHO_RESUME',			#恢复SE	client.adjust_param('STRESSECHO_RESUME')
                    'stressecho_acquire':'STRESSECHO_ACQUIRE',			#采集	client.adjust_param('STRESSECHO_ACQUIRE')
                    'stressecho_re_acquire':'STRESSECHO_RE_ACQUIRE',			#重新采集	client.adjust_param('STRESSECHO_RE_ACQUIRE')
                    'stressecho_show_selected':'STRESSECHO_SHOW_SELECTED',			#显示已选择	client.adjust_param('STRESSECHO_SHOW_SELECTED')
                    'stressecho_accept_selected':'STRESSECHO_ACCEPT_SELECTED',			#接受选择	client.adjust_param('STRESSECHO_ACCEPT_SELECTED')
                    'stressecho_pause':'STRESSECHO_PAUSE',			#暂停采集	client.adjust_param('STRESSECHO_PAUSE')
                    'stressecho_end_acquire':'STRESSECHO_END_ACQUIRE',			#结束采集	client.adjust_param('STRESSECHO_END_ACQUIRE')
                    'stressecho_end_stage':'STRESSECHO_END_STAGE',			#结束阶段	client.adjust_param('STRESSECHO_END_STAGE')
                    'stressecho_select_clip1':'STRESSECHO_SELECT_CLIP1',			#选定影像1	client.adjust_param('STRESSECHO_SELECT_CLIP1')
                    'stressecho_select_clip2':'STRESSECHO_SELECT_CLIP2',			#选定影像2	client.adjust_param('STRESSECHO_SELECT_CLIP2')
                    'stressecho_select_clip3':'STRESSECHO_SELECT_CLIP3',			#选定影像3	client.adjust_param('STRESSECHO_SELECT_CLIP3')
                    'stressecho_select_clip4':'STRESSECHO_SELECT_CLIP4',			#选定影像4	client.adjust_param('STRESSECHO_SELECT_CLIP4')
                    'stressecho_shuffle_up':'STRESSECHO_SHUFFLE_UP',			#向右切换对比方式	client.adjust_param('STRESSECHO_SHUFFLE_UP')
                    'stressecho_shuffle_down':'STRESSECHO_SHUFFLE_DOWN',			#向左切换对比方式	client.adjust_param('STRESSECHO_SHUFFLE_DOWN')
                    'stressecho_page_changed_up':'STRESSECHO_PAGE_CHANGED_UP',			#向前翻页	client.adjust_param('STRESSECHO_PAGE_CHANGED_UP')
                    'stressecho_page_changed_down':'STRESSECHO_PAGE_CHANGED_DOWN',			#向后翻页	client.adjust_param('STRESSECHO_PAGE_CHANGED_DOWN')
                    'stressecho_stage_up':'STRESSECHO_STAGE_UP',			#向右切换阶段	client.adjust_param('STRESSECHO_STAGE_UP')
                    'stressecho_stage_down':'STRESSECHO_STAGE_DOWN',			#向左切换阶段	client.adjust_param('STRESSECHO_STAGE_DOWN')
                    'stressecho_set_all_normal':'STRESSECHO_SET_ALL_NORMAL',			#设置所有节段正常	client.adjust_param('STRESSECHO_SET_ALL_NORMAL')
                    'stressecho_set_all_not_scored':'STRESSECHO_SET_ALL_NOT_SCORED',			#设置所有节段默认	client.adjust_param('STRESSECHO_SET_ALL_NOT_SCORED')
                    # B-3D4D
                    '3dpa_label_4d':'3DPA_LABEL_4D',			#开启4D预激活模式	client.adjust_param('3DPA_LABEL_4D')
                    '4dpa_user_mode1/surface':'4DPA_USER_MODE1/SURFACE',			#开启4D第一个用户模式	client.adjust_param('4DPA_USER_MODE1/SURFACE')
                    '4dpa_user_mode2/skeleton':'4DPA_USER_MODE2/SKELETON',			#开启4D第二个用户模式	client.adjust_param('4DPA_USER_MODE2/SKELETON')
                    '4dpa_user_mode3':'4DPA_USER_MODE3',			#开启4D第三个用户模式	client.adjust_param('4DPA_USER_MODE3')
                    '4dpa_user_mode4':'4DPA_USER_MODE4',			#开启4D第四个用户模式	client.adjust_param('4DPA_USER_MODE4')
                    '4dpa_disp_full':'4DPA_DISP_FULL',			#4D预激活单幅显示	client.adjust_param('4DPA_DISP_FULL')
                    '4dpa_disp_dual':'4DPA_DISP_DUAL',			#4D预激活双幅显示	client.adjust_param('4DPA_DISP_DUAL')
                    '4dpa_disp_quad':'4DPA_DISP_QUAD',			#4D预激活四幅显示	client.adjust_param('4DPA_DISP_QUAD')
                    '4dpa_focus_up':'4DPA_FOCUS_UP',			#增大4D焦点位置	client.adjust_param('4DPA_FOCUS_UP')
                    '4dpa_focus_down':'4DPA_FOCUS_DOWN',			#减小4D焦点位置	client.adjust_param('4DPA_FOCUS_DOWN')
                    '4dpa_image_quality_up':'4DPA_IMAGE_QUALITY_UP',			#增大4D图像质量	client.adjust_param('4DPA_IMAGE_QUALITY_UP')
                    '4dpa_image_quality_down':'4DPA_IMAGE_QUALITY_DOWN',			#减小4D图像质量	client.adjust_param('4DPA_IMAGE_QUALITY_DOWN')
                    '4dpa_sweep_angle_up':'4DPA_SWEEP_ANGLE_UP',			#增大4D摆动角度	client.adjust_param('4DPA_SWEEP_ANGLE_UP')
                    '4dpa_sweep_angle_down':'4DPA_SWEEP_ANGLE_DOWN',			#减小4D摆动角度	client.adjust_param('4DPA_SWEEP_ANGLE_DOWN')
                    '4dpa_stalility_up':'4DPA_STALILITY_UP',			#开启4D稳定性	client.adjust_param('4DPA_STALILITY_UP')
                    '4dpa_stalility_down':'4DPA_STALILITY_DOWN',			#关闭4D稳定性	client.adjust_param('4DPA_STALILITY_DOWN')
                    '4dpa_start':'4DPA_START',			#开启4D实时模式	client.adjust_param('4DPA_START')
                    '3d_menu_page_down':'3D_MENU_PAGE_DOWN',			#4D向下翻页	client.adjust_param('3D_MENU_PAGE_DOWN')
                    '4drt_render_surface':'4DRT_RENDER_SURFACE',			#开启4D表面成像渲染模式	client.adjust_param('4DRT_RENDER_SURFACE')
                    '3d_menu_page_up':'3D_MENU_PAGE_UP',			#4D向上翻页	client.adjust_param('3D_MENU_PAGE_UP')
                    '4drt_edit_roi':'4DRT_EDIT_ROI',			#编辑ROI锁定4D视图	client.adjust_param('4DRT_EDIT_ROI')
                    '4drt_inversion':'4DRT_INVERSION',			#反转4D成像	client.adjust_param('4DRT_INVERSION')
                    '4drt_rotate':'4DRT_ROTATE',			#自由旋转4D成像	client.adjust_param('4DRT_ROTATE')
                    '4drt_disp_full':'4DRT_DISP_FULL',			#4D实时单幅显示	client.adjust_param('4DRT_DISP_FULL')
                    '4drt_disp_dual':'4DRT_DISP_DUAL',			#4D实时双幅显示	client.adjust_param('4DRT_DISP_DUAL')
                    '4drt_disp_quad':'4DRT_DISP_QUAD',			#4D实时四幅显示	client.adjust_param('4DRT_DISP_QUAD')
                    '4drt_orient_90':'4DRT_ORIENT_90',			#90度旋转4D	client.adjust_param('4DRT_ORIENT_90')
                    '4drt_orient_270':'4DRT_ORIENT_270',			#270度旋转4D	client.adjust_param('4DRT_ORIENT_270')
                    '4drt_reset':'4DRT_RESET',			#复位4D	client.adjust_param('4DRT_RESET')
                    '4drt_orient_180':'4DRT_ORIENT_180',			#180度旋转4D	client.adjust_param('4DRT_ORIENT_180')
                    '4drt_orient_0':'4DRT_ORIENT_0',			#0度旋转4D	client.adjust_param('4DRT_ORIENT_0')
                    '4drt_slice_b':'4DRT_SLICE_B',			#选择4D的B视图	client.adjust_param('4DRT_SLICE_B')
                    '4drt_slice_3d':'4DRT_SLICE_3D',			#选择3D图像	client.adjust_param('4DRT_SLICE_3D')
                    '4drt_slice_c':'4DRT_SLICE_C',			#选择4D的C视图	client.adjust_param('4DRT_SLICE_C')
                    '4drt_slice_a':'4DRT_SLICE_A',			#选择4D的A视图	client.adjust_param('4DRT_SLICE_A')
                    '4drt_threshold_down':'4DRT_THRESHOLD_DOWN',			#减小4D阈值	client.adjust_param('4DRT_THRESHOLD_DOWN')
                    '4drt_threshold_up':'4DRT_THRESHOLD_UP',			#增大4D阈值	client.adjust_param('4DRT_THRESHOLD_UP')
                    '4drt_contrast_down':'4DRT_CONTRAST_DOWN',			#减小4D的对比度	client.adjust_param('4DRT_CONTRAST_DOWN')
                    '4drt_contrast_up':'4DRT_CONTRAST_UP',			#增大4D的对比度	client.adjust_param('4DRT_CONTRAST_UP')
                    '4drt_transparency_up':'4DRT_TRANSPARENCY_UP',			#增大4D的透明度	client.adjust_param('4DRT_TRANSPARENCY_UP')
                    '4drt_transparency_down':'4DRT_TRANSPARENCY_DOWN',			#减小4D的透明度	client.adjust_param('4DRT_TRANSPARENCY_DOWN')
                    '4drt_brightness_down':'4DRT_BRIGHTNESS_DOWN',			#减小4D亮度	client.adjust_param('4DRT_BRIGHTNESS_DOWN')
                    '4drt_brightness_up':'4DRT_BRIGHTNESS_UP',			#增大4D亮度	client.adjust_param('4DRT_BRIGHTNESS_UP')
                    '4drt_smoothness_down':'4DRT_SMOOTHNESS_DOWN',			#减小4D平滑值	client.adjust_param('4DRT_SMOOTHNESS_DOWN')
                    '4drt_smoothness_up':'4DRT_SMOOTHNESS_UP',			#增大4D平滑值	client.adjust_param('4DRT_SMOOTHNESS_UP')
                    '4drt_2duscan_down':'4DRT_2DUSCAN_DOWN',			#减小4D的2D微米成像值	client.adjust_param('4DRT_2DUSCAN_DOWN')
                    '4drt_2duscan_up':'4DRT_2DUSCAN_UP',			#增大4D的2D微米成像值	client.adjust_param('4DRT_2DUSCAN_UP')
                    '4drt_3duscan_down':'4DRT_3DUSCAN_DOWN',			#减小4D的3D微米成像值	client.adjust_param('4DRT_3DUSCAN_DOWN')
                    '4drt_3duscan_up':'4DRT_3DUSCAN_UP',			#增大4D的3D微米成像值	client.adjust_param('4DRT_3DUSCAN_UP')
                    '4drt_3dchroma_down':'4DRT_3DCHROMA_DOWN',			#减小4D的3D伪彩值	client.adjust_param('4DRT_3DCHROMA_DOWN')
                    '4drt_3dchroma_up':'4DRT_3DCHROMA_UP',			#增大4D的3D伪彩值	client.adjust_param('4DRT_3DCHROMA_UP')
                    '4drt_bchroma_down':'4DRT_BCHROMA_DOWN',			#减小4D的B伪彩值	client.adjust_param('4DRT_BCHROMA_DOWN')
                    '4drt_bchroma_up':'4DRT_BCHROMA_UP',			#增大4D的B伪彩值	client.adjust_param('4DRT_BCHROMA_UP')
                    '4drt_render_grad_light':'4DRT_RENDER_GRAD_LIGHT',			#开启4D梯度亮度渲染模式	client.adjust_param('4DRT_RENDER_GRAD_LIGHT')
                    '4drt_render_skeleton':'4DRT_RENDER_SKELETON',			#开启4D骨骼成像渲染模式	client.adjust_param('4DRT_RENDER_SKELETON')
                    '4drt_skeleton_depth':'4DRT_SKELETON_DEPTH',			#开启4D骨骼深度成像	client.adjust_param('4DRT_SKELETON_DEPTH')
                    '4drt_skeleton':'4DRT_SKELETON',			#开启4D骨骼成像	client.adjust_param('4DRT_SKELETON')
                    '4drt_render_transp_min':'4DRT_RENDER_TRANSP_MIN',			#开启4D最小回声成像渲染模式	client.adjust_param('4DRT_RENDER_TRANSP_MIN')
                    '4drt_render_xray':'4DRT_RENDER_XRAY',			#开启4D的X-线成像渲染模式	client.adjust_param('4DRT_RENDER_XRAY')
                    '4drt_render_sdepth':'4DRT_RENDER_SDEPTH',			#开启4D深度成像渲染模式	client.adjust_param('4DRT_RENDER_SDEPTH')
                    '4drt_render_slive':'4DRT_RENDER_SLIVE',			#开启4D的S-Live渲染模式	client.adjust_param('4DRT_RENDER_SLIVE')
                    '4drt_light_pos_down':'4DRT_LIGHT_POS_DOWN',			#调小4D灯光位置	client.adjust_param('4DRT_LIGHT_POS_DOWN')
                    '4drt_light_pos_up':'4DRT_LIGHT_POS_UP',			#调大4D灯光位置	client.adjust_param('4DRT_LIGHT_POS_UP')
                    '4drt_slive_silhouette':'4DRT_SLIVE_SILHOUETTE',			#开启4D的S-Live Silhouette结构	client.adjust_param('4DRT_SLIVE_SILHOUETTE')
                    '4drt_edit_light':'4DRT_EDIT_LIGHT',			#开启4D调节灯光功能	client.adjust_param('4DRT_EDIT_LIGHT')
                    '4drt_slive':'4DRT_SLIVE',			#开启4D的S-Live结构	client.adjust_param('4DRT_SLIVE')
                    '4drt_label_view':'4DRT_LABEL_VIEW',			#开启4D的视图页签	client.adjust_param('4DRT_LABEL_VIEW')
                    '4drt_direction_left':'4DRT_DIRECTION_LEFT',			#4D左侧视图	client.adjust_param('4DRT_DIRECTION_LEFT')
                    '4drt_direction_fornt':'4DRT_DIRECTION_FORNT',			#4D前面视图	client.adjust_param('4DRT_DIRECTION_FORNT')
                    '4drt_direction_back':'4DRT_DIRECTION_BACK',			#4D后面视图	client.adjust_param('4DRT_DIRECTION_BACK')
                    '4drt_direction_right':'4DRT_DIRECTION_RIGHT',			#4D右侧视图	client.adjust_param('4DRT_DIRECTION_RIGHT')
                    '4drt_direction_bottom':'4DRT_DIRECTION_BOTTOM',			#4D底部视图	client.adjust_param('4DRT_DIRECTION_BOTTOM')
                    '4drt_direction_top':'4DRT_DIRECTION_TOP',			#4D顶部视图	client.adjust_param('4DRT_DIRECTION_TOP')
                    '4drt_rotatex_up':'4DRT_ROTATEX_UP',			#增大4D的X旋转角度	client.adjust_param('4DRT_ROTATEX_UP')
                    '4drt_rotatex_down':'4DRT_ROTATEX_DOWN',			#减小4D的X旋转角度	client.adjust_param('4DRT_ROTATEX_DOWN')
                    '4drt_rotatey_up':'4DRT_ROTATEY_UP',			#增大4D的Y旋转角度	client.adjust_param('4DRT_ROTATEY_UP')
                    '4drt_rotatey_down':'4DRT_ROTATEY_DOWN',			#减小4D的Y旋转角度	client.adjust_param('4DRT_ROTATEY_DOWN')
                    '4drt_rotatez_up':'4DRT_ROTATEZ_UP',			#增大4D的Z旋转角度	client.adjust_param('4DRT_ROTATEZ_UP')
                    '4drt_rotatez_down':'4DRT_ROTATEZ_DOWN',			#减小4D的Z旋转角度	client.adjust_param('4DRT_ROTATEZ_DOWN')
                    '4drt_moveud_up':'4DRT_MOVEUD_UP',			#4D向上移动	client.adjust_param('4DRT_MOVEUD_UP')
                    '4drt_moveud_down':'4DRT_MOVEUD_DOWN',			#4D向下移动	client.adjust_param('4DRT_MOVEUD_DOWN')
                    '4drt_movelr_up':'4DRT_MOVELR_UP',			#4D向右移动	client.adjust_param('4DRT_MOVELR_UP')
                    '4drt_movelr_down':'4DRT_MOVELR_DOWN',			#4D向左移动	client.adjust_param('4DRT_MOVELR_DOWN')
                    '4drt_label_3d4d':'4DRT_LABEL_3D4D',			#开启3D4D页签	client.adjust_param('4DRT_LABEL_3D4D')
                    '4drt_volpre':'4DRT_VOLPRE',			#返回4D预激活模式	client.adjust_param('4DRT_VOLPRE')
                    '4dpa_label_3d':'4DPA_LABEL_3D',			#开启3D预激活模式	client.adjust_param('4DPA_LABEL_3D')
                    '3dpa_user_mode1_surface':'3DPA_USER_MODE1/SURFACE',			#开启3D第一个用户模式	client.adjust_param('3DPA_USER_MODE1/SURFACE')
                    '3dpa_user_mode2_skeleton':'3DPA_USER_MODE2/SKELETON',			#开启3D第二个用户模式	client.adjust_param('3DPA_USER_MODE2/SKELETON')
                    '3dpa_user_mode3':'3DPA_USER_MODE3',			#开启3D第三个用户模式	client.adjust_param('3DPA_USER_MODE3')
                    '3dpa_user_mode4':'3DPA_USER_MODE4',			#开启3D第四个用户模式	client.adjust_param('3DPA_USER_MODE4')
                    '3dpa_disp_full':'3DPA_DISP_FULL',			#3D预激活单幅显示	client.adjust_param('3DPA_DISP_FULL')
                    '3dpa_disp_dual':'3DPA_DISP_DUAL',			#3D预激活双幅显示	client.adjust_param('3DPA_DISP_DUAL')
                    '3dpa_disp_quad':'3DPA_DISP_QUAD',			#3D预激活四幅显示	client.adjust_param('3DPA_DISP_QUAD')
                    '3dpa_focus_down':'3DPA_FOCUS_DOWN',			#减小3D焦点位置	client.adjust_param('3DPA_FOCUS_DOWN')
                    '3dpa_focus_up':'3DPA_FOCUS_UP',			#增大3D焦点位置	client.adjust_param('3DPA_FOCUS_UP')
                    '3dpa_image_quality_down':'3DPA_IMAGE_QUALITY_DOWN',			#减小3D图像质量	client.adjust_param('3DPA_IMAGE_QUALITY_DOWN')
                    '3dpa_image_quality_up':'3DPA_IMAGE_QUALITY_UP',			#增大3D图像质量	client.adjust_param('3DPA_IMAGE_QUALITY_UP')
                    '3dpa_sweep_angle_down':'3DPA_SWEEP_ANGLE_DOWN',			#减小3D摆动角度	client.adjust_param('3DPA_SWEEP_ANGLE_DOWN')
                    '3dpa_sweep_angle_up':'3DPA_SWEEP_ANGLE_UP',			#增大3D摆动角度	client.adjust_param('3DPA_SWEEP_ANGLE_UP')
                    '3dpa_start':'3DPA_START',			#开启3D实时模式	client.adjust_param('3DPA_START')
                    '3dfz_label_3d4d':'3DFZ_LABEL_3D4D',			#进入3D/4D页签	client.adjust_param('3DFZ_LABEL_3D4D')
                    '3dfz_edit_roi':'3DFZ_EDIT_ROI',			#编辑ROI锁定3D视图	client.adjust_param('3DFZ_EDIT_ROI')
                    '3dfz_inversion':'3DFZ_INVERSION',			#反转3D成像	client.adjust_param('3DFZ_INVERSION')
                    '3dfz_rotate':'3DFZ_ROTATE',			#自由旋转3D成像	client.adjust_param('3DFZ_ROTATE')
                    '3dfz_autoface':'3DFZ_AUTOFACE',			#一键显脸	client.adjust_param('3DFZ_AUTOFACE')
                    '3dfz_disp_full':'3DFZ_DISP_FULL',			#3D实时单幅显示	client.adjust_param('3DFZ_DISP_FULL')
                    '3dfz_disp_dual':'3DFZ_DISP_DUAL',			#3D实时双幅显示	client.adjust_param('3DFZ_DISP_DUAL')
                    '3dfz_disp_quad':'3DFZ_DISP_QUAD',			#3D实时四幅显示	client.adjust_param('3DFZ_DISP_QUAD')
                    '3dfz_orient_90':'3DFZ_ORIENT_90',			#90度旋转3D	client.adjust_param('3DFZ_ORIENT_90')
                    '3dfz_orient_270':'3DFZ_ORIENT_270',			#270度旋转3D	client.adjust_param('3DFZ_ORIENT_270')
                    '3dfz_reset':'3DFZ_RESET',			#复位3D	client.adjust_param('3DFZ_RESET')
                    '3dfz_orient_180':'3DFZ_ORIENT_180',			#180度旋转3D	client.adjust_param('3DFZ_ORIENT_180')
                    '3dfz_orient_0':'3DFZ_ORIENT_0',			#0度旋转3D	client.adjust_param('3DFZ_ORIENT_0')
                    '3dfz_slice_b':'3DFZ_SLICE_B',			#选择3D的B视图	client.adjust_param('3DFZ_SLICE_B')
                    '3dfz_slice_3d':'3DFZ_SLICE_3D',			#选择3D图像	client.adjust_param('3DFZ_SLICE_3D')
                    '3dfz_slice_c':'3DFZ_SLICE_C',			#选择3D的C视图	client.adjust_param('3DFZ_SLICE_C')
                    '3dfz_slice_a':'3DFZ_SLICE_A',			#选择3D的A视图	client.adjust_param('3DFZ_SLICE_A')
                    '3dfz_render_surface':'3DFZ_RENDER_SURFACE',			#开启3D表面成像渲染模式	client.adjust_param('3DFZ_RENDER_SURFACE')
                    '3dfz_threshold_down':'3DFZ_THRESHOLD_DOWN',			#减小3D阈值	client.adjust_param('3DFZ_THRESHOLD_DOWN')
                    '3dfz_threshold_up':'3DFZ_THRESHOLD_UP',			#增大3D阈值	client.adjust_param('3DFZ_THRESHOLD_UP')
                    '3dfz_contrast_down':'3DFZ_CONTRAST_DOWN',			#减小3D的对比度	client.adjust_param('3DFZ_CONTRAST_DOWN')
                    '3dfz_contrast_up':'3DFZ_CONTRAST_UP',			#增大3D的对比度	client.adjust_param('3DFZ_CONTRAST_UP')
                    '3dfz_transparency_down':'3DFZ_TRANSPARENCY_DOWN',			#减小3D的透明度	client.adjust_param('3DFZ_TRANSPARENCY_DOWN')
                    '3dfz_transparency_up':'3DFZ_TRANSPARENCY_UP',			#增大3D的透明度	client.adjust_param('3DFZ_TRANSPARENCY_UP')
                    '3dfz_brightness_down':'3DFZ_BRIGHTNESS_DOWN',			#减小3D亮度	client.adjust_param('3DFZ_BRIGHTNESS_DOWN')
                    '3dfz_brightness_up':'3DFZ_BRIGHTNESS_UP',			#增大3D亮度	client.adjust_param('3DFZ_BRIGHTNESS_UP')
                    '3dfz_smoothness_down':'3DFZ_SMOOTHNESS_DOWN',			#减小3D平滑值	client.adjust_param('3DFZ_SMOOTHNESS_DOWN')
                    '3dfz_smoothness_up':'3DFZ_SMOOTHNESS_UP',			#增大3D平滑值	client.adjust_param('3DFZ_SMOOTHNESS_UP')
                    '3dfz_2duscan_down':'3DFZ_2DUSCAN_DOWN',			#减小3D的2D微米成像值	client.adjust_param('3DFZ_2DUSCAN_DOWN')
                    '3dfz_2duscan_up':'3DFZ_2DUSCAN_UP',			#增大3D的2D微米成像值	client.adjust_param('3DFZ_2DUSCAN_UP')
                    '3dfz_3duscan_down':'3DFZ_3DUSCAN_DOWN',			#减小3D的3D微米成像值	client.adjust_param('3DFZ_3DUSCAN_DOWN')
                    '3dfz_3duscan_up':'3DFZ_3DUSCAN_UP',			#增大3D的3D微米成像值	client.adjust_param('3DFZ_3DUSCAN_UP')
                    '3dfz_3dchroma_down':'3DFZ_3DCHROMA_DOWN',			#减小3D的3D伪彩值	client.adjust_param('3DFZ_3DCHROMA_DOWN')
                    '3dfz_3dchroma_up':'3DFZ_3DCHROMA_UP',			#增大3D的3D伪彩值	client.adjust_param('3DFZ_3DCHROMA_UP')
                    '3dfz_bchroma_down':'3DFZ_BCHROMA_DOWN',			#减小3D的B伪彩值	client.adjust_param('3DFZ_BCHROMA_DOWN')
                    '3dfz_bchroma_up':'3DFZ_BCHROMA_UP',			#增大3D的B伪彩值	client.adjust_param('3DFZ_BCHROMA_UP')
                    '3dfz_label_cplane':'3DFZ_LABEL_CPLANE',			#开启3D截面页签	client.adjust_param('3DFZ_LABEL_CPLANE')
                    '3dfz_cp_2duscan_down':'3DFZ_CP_2DUSCAN_DOWN',			#减小3D截面2D微米成像	client.adjust_param('3DFZ_CP_2DUSCAN_DOWN')
                    '3dfz_cp_2duscan_up':'3DFZ_CP_2DUSCAN_UP',			#增大3D截面2D微米成像	client.adjust_param('3DFZ_CP_2DUSCAN_UP')
                    '3dfz_render_grad_light':'3DFZ_RENDER_GRAD_LIGHT',			#开启3D梯度亮度渲染模式	client.adjust_param('3DFZ_RENDER_GRAD_LIGHT')
                    '3dfz_render_skeleton':'3DFZ_RENDER_SKELETON',			#开启3D骨骼成像渲染模式	client.adjust_param('3DFZ_RENDER_SKELETON')
                    '3dfz_skeleton_depth':'3DFZ_SKELETON_DEPTH',			#开启3D骨骼深度成像	client.adjust_param('3DFZ_SKELETON_DEPTH')
                    '3dfz_skeleton':'3DFZ_SKELETON',			#开启3D骨骼成像	client.adjust_param('3DFZ_SKELETON')
                    '3dfz_render_transp_min':'3DFZ_RENDER_TRANSP_MIN',			#开启3D最小回声成像渲染模式	client.adjust_param('3DFZ_RENDER_TRANSP_MIN')
                    '3dfz_render_xray':'3DFZ_RENDER_XRAY',			#开启3D的X-线成像渲染模式	client.adjust_param('3DFZ_RENDER_XRAY')
                    '3dfz_render_sdepth':'3DFZ_RENDER_SDEPTH',			#开启3D深度成像渲染模式	client.adjust_param('3DFZ_RENDER_SDEPTH')
                    '3dfz_render_slive':'3DFZ_RENDER_SLIVE',			#开启3D的S-Live渲染模式	client.adjust_param('3DFZ_RENDER_SLIVE')
                    '3dfz_light_pos_down':'3DFZ_LIGHT_POS_DOWN',			#减小3D的灯光位置	client.adjust_param('3DFZ_LIGHT_POS_DOWN')
                    '3dfz_light_pos_up':'3DFZ_LIGHT_POS_UP',			#增大3D的灯光位置	client.adjust_param('3DFZ_LIGHT_POS_UP')
                    '3dfz_slive_silhouette':'3DFZ_SLIVE_SILHOUETTE',			#开启3D的S-Live Silhouette结构	client.adjust_param('3DFZ_SLIVE_SILHOUETTE')
                    '3dfz_edit_light':'3DFZ_EDIT_LIGHT',			#开启3D调节灯光功能	client.adjust_param('3DFZ_EDIT_LIGHT')
                    '3dfz_slive':'3DFZ_SLIVE',			#开启3D的S-Live结构	client.adjust_param('3DFZ_SLIVE')
                    '3dfz_label_view':'3DFZ_LABEL_VIEW',			#开启3D的视图页签	client.adjust_param('3DFZ_LABEL_VIEW')
                    '3dfz_rotate_45':'3DFZ_ROTATE_45',			#45度自由旋转3D成像	client.adjust_param('3DFZ_ROTATE_45')
                    '3dfz_rotate_90':'3DFZ_ROTATE_90',			#90度自由旋转3D成像	client.adjust_param('3DFZ_ROTATE_90')
                    '3dfz_rotate_360':'3DFZ_ROTATE_360',			#360度自由旋转3D成像	client.adjust_param('3DFZ_ROTATE_360')
                    '3dfz_rotate_270':'3DFZ_ROTATE_270',			#270度自由旋转3D成像	client.adjust_param('3DFZ_ROTATE_270')
                    '3dfz_rotate_180':'3DFZ_ROTATE_180',			#180度自由旋转3D成像	client.adjust_param('3DFZ_ROTATE_180')
                    '3dfz_rotate_0':'3DFZ_ROTATE_0',			#0度自由旋转3D成像	client.adjust_param('3DFZ_ROTATE_0')
                    '3dfz_direction_left':'3DFZ_DIRECTION_LEFT',			#3D左侧视图	client.adjust_param('3DFZ_DIRECTION_LEFT')
                    '3dfz_direction_fornt':'3DFZ_DIRECTION_FORNT',			#3D前面视图	client.adjust_param('3DFZ_DIRECTION_FORNT')
                    '3dfz_direction_back':'3DFZ_DIRECTION_BACK',			#3D后面视图	client.adjust_param('3DFZ_DIRECTION_BACK')
                    '3dfz_direction_right':'3DFZ_DIRECTION_RIGHT',			#3D右侧视图	client.adjust_param('3DFZ_DIRECTION_RIGHT')
                    '3dfz_direction_bottom':'3DFZ_DIRECTION_BOTTOM',			#3D底部视图	client.adjust_param('3DFZ_DIRECTION_BOTTOM')
                    '3dfz_direction_top':'3DFZ_DIRECTION_TOP',			#3D顶部视图	client.adjust_param('3DFZ_DIRECTION_TOP')
                    '3dfz_rotatex_up':'3DFZ_ROTATEX_UP',			#增大3D的X旋转角度	client.adjust_param('3DFZ_ROTATEX_UP')
                    '3dfz_rotatex_down':'3DFZ_ROTATEX_DOWN',			#减小3D的X旋转角度	client.adjust_param('3DFZ_ROTATEX_DOWN')
                    '3dfz_rotatey_up':'3DFZ_ROTATEY_UP',			#增大3D的Y旋转角度	client.adjust_param('3DFZ_ROTATEY_UP')
                    '3dfz_rotatey_down':'3DFZ_ROTATEY_DOWN',			#减小3D的Y旋转角度	client.adjust_param('3DFZ_ROTATEY_DOWN')
                    '3dfz_rotatez_up':'3DFZ_ROTATEZ_UP',			#增大3D的Z旋转角度	client.adjust_param('3DFZ_ROTATEZ_UP')
                    '3dfz_rotatez_down':'3DFZ_ROTATEZ_DOWN',			#减小3D的Z旋转角度	client.adjust_param('3DFZ_ROTATEZ_DOWN')
                    '3dfz_moveud_up':'3DFZ_MOVEUD_UP',			#3D向上移动	client.adjust_param('3DFZ_MOVEUD_UP')
                    '3dfz_moveud_down':'3DFZ_MOVEUD_DOWN',			#3D向下移动	client.adjust_param('3DFZ_MOVEUD_DOWN')
                    '3dfz_movelr_up':'3DFZ_MOVELR_UP',			#3D向右移动	client.adjust_param('3DFZ_MOVELR_UP')
                    '3dfz_movelr_down':'3DFZ_MOVELR_DOWN',			#3D向左移动	client.adjust_param('3DFZ_MOVELR_DOWN')
                    '3dfz_label_edit':'3DFZ_LABEL_EDIT',			#开启3D编辑页签	client.adjust_param('3DFZ_LABEL_EDIT')
                    '3dfz_edit_rotate':'3DFZ_EDIT_ROTATE',			#自由旋转3D成像	client.adjust_param('3DFZ_EDIT_ROTATE')
                    '3dfz_cut_method1_trancein':'3DFZ_CUT_METHOD1/TRANCEIN',			#3D描迹剪切区域内部分	client.adjust_param('3DFZ_CUT_METHOD1/TRANCEIN')
                    '3dfz_cut_method3_boxin':'3DFZ_CUT_METHOD3/BOXIN',			#3D方框剪切区域内部分	client.adjust_param('3DFZ_CUT_METHOD3/BOXIN')
                    '3dfz_cut_method6_bigeraser':'3DFZ_CUT_METHOD6/BIGERASER',			#3D大橡皮擦剪切	client.adjust_param('3DFZ_CUT_METHOD6/BIGERASER')
                    '3dfz_cut_method5_samlleraser':'3DFZ_CUT_METHOD5/SAMLLERASER',			#3D小橡皮擦剪切	client.adjust_param('3DFZ_CUT_METHOD5/SAMLLERASER')
                    '3dfz_cut_method4_boxout':'3DFZ_CUT_METHOD4/BOXOUT',			#3D方框剪切区域外部分	client.adjust_param('3DFZ_CUT_METHOD4/BOXOUT')
                    '3dfz_cut_method2_tranceout':'3DFZ_CUT_METHOD2/TRANCEOUT',			#3D描迹剪切区域外部分	client.adjust_param('3DFZ_CUT_METHOD2/TRANCEOUT')
                    '3dfz_disp_ab':'3DFZ_DISP_AB',			#显示3D的AB视图	client.adjust_param('3DFZ_DISP_AB')
                    '3dfz_cp_slice_b':'3DFZ_CP_SLICE_B',			#选择3D的B视图进行层切	client.adjust_param('3DFZ_CP_SLICE_B')
                    '3dfz_cp_slice_a':'3DFZ_CP_SLICE_A',			#选择3D的A视图进行层切	client.adjust_param('3DFZ_CP_SLICE_A')
                    '3dfz_disp_ac':'3DFZ_DISP_AC',			#显示3D的AC视图	client.adjust_param('3DFZ_DISP_AC')
                    '3dfz_cp_slice_c':'3DFZ_CP_SLICE_C',			#选择3D的C视图进行层切	client.adjust_param('3DFZ_CP_SLICE_C')
                    '3dfz_disp_bc':'3DFZ_DISP_BC',			#显示3D的BC视图	client.adjust_param('3DFZ_DISP_BC')
                    '3dfz_disp_abc':'3DFZ_DISP_ABC',			#显示3D的ABC视图	client.adjust_param('3DFZ_DISP_ABC')
                    '3dfz_cp_bchroma_down':'3DFZ_CP_BCHROMA_DOWN',			#减小3D的B伪彩值	client.adjust_param('3DFZ_CP_BCHROMA_DOWN')
                    '3dfz_cp_bchroma_up':'3DFZ_CP_BCHROMA_UP',			#增大3D的B伪彩值	client.adjust_param('3DFZ_CP_BCHROMA_UP')
                    '3dfz_label_mslice':'3DFZ_LABEL_MSLICE',			#开启3D的断层切片页签	client.adjust_param('3DFZ_LABEL_MSLICE')
                    '3dfz_ms_slice_b':'3DFZ_MS_SLICE_B',			#选择3D的B切片平面	client.adjust_param('3DFZ_MS_SLICE_B')
                    '3dfz_ms_slice_c':'3DFZ_MS_SLICE_C',			#选择3D的C切片平面	client.adjust_param('3DFZ_MS_SLICE_C')
                    '3dfz_ms_slice_a':'3DFZ_MS_SLICE_A',			#选择3D的A切片平面	client.adjust_param('3DFZ_MS_SLICE_A')
                    '3dfz_disp_12':'3DFZ_DISP_12',			#设置3D显示模式为1*2	client.adjust_param('3DFZ_DISP_12')
                    '3dfz_disp_33':'3DFZ_DISP_33',			#设置3D显示模式为3*3	client.adjust_param('3DFZ_DISP_33')
                    '3dfz_disp_44':'3DFZ_DISP_44',			#设置3D显示模式为4*4	client.adjust_param('3DFZ_DISP_44')
                    '3dfz_disp_55':'3DFZ_DISP_55',			#设置3D显示模式为5*5	client.adjust_param('3DFZ_DISP_55')
                    '3dfz_disp_34':'3DFZ_DISP_34',			#设置3D显示模式为3*4	client.adjust_param('3DFZ_DISP_34')
                    '3dfz_disp_22':'3DFZ_DISP_22',			#设置3D显示模式为2*2	client.adjust_param('3DFZ_DISP_22')
                    '3dfz_ms_bchroma_down':'3DFZ_MS_BCHROMA_DOWN',			#减小3D断层切片的B伪彩值	client.adjust_param('3DFZ_MS_BCHROMA_DOWN')
                    '3dfz_ms_bchroma_up':'3DFZ_MS_BCHROMA_UP',			#增大3D断层切片的B伪彩值	client.adjust_param('3DFZ_MS_BCHROMA_UP')
                    '3dfz_ms_adjustpos_down':'3DFZ_MS_ADJUSTPOS_DOWN',			#微减小3D所选切片的位置	client.adjust_param('3DFZ_MS_ADJUSTPOS_DOWN')
                    '3dfz_ms_adjustpos_up':'3DFZ_MS_ADJUSTPOS_UP',			#微增大3D所选切片的位置	client.adjust_param('3DFZ_MS_ADJUSTPOS_UP')
                    '3dfz_ms_distance_down':'3DFZ_MS_DISTANCE_DOWN',			#减小3D切片间距	client.adjust_param('3DFZ_MS_DISTANCE_DOWN')
                    '3dfz_ms_distance_up':'3DFZ_MS_DISTANCE_UP',			#增大3D切片间距	client.adjust_param('3DFZ_MS_DISTANCE_UP')
                    '3dfz_ms_slicenum_down':'3DFZ_MS_SLICENUM_DOWN',			#减少3D切片数量	client.adjust_param('3DFZ_MS_SLICENUM_DOWN')
                    '3dfz_ms_slicenum_up':'3DFZ_MS_SLICENUM_UP',			#增多3D切片数量	client.adjust_param('3DFZ_MS_SLICENUM_UP')
                    '3dfz_ms_display_down':'3DFZ_MS_DISPLAY_DOWN',			#向左平移3D切片区域所有切片	client.adjust_param('3DFZ_MS_DISPLAY_DOWN')
                    '3dfz_ms_display_up':'3DFZ_MS_DISPLAY_UP',			#向右平移3D切片区域所有切片	client.adjust_param('3DFZ_MS_DISPLAY_UP')
                    '3dfz_label_avc':'3DFZ_LABEL_AVC',			#开启3D卵泡自动测量页签	client.adjust_param('3DFZ_LABEL_AVC')
                    '3dfz_leftovary':'3DFZ_LEFTOVARY',			#开启3D左侧卵巢	client.adjust_param('3DFZ_LEFTOVARY')
                    '3dfz_rightovary':'3DFZ_RIGHTOVARY',			#开启3D右侧卵巢	client.adjust_param('3DFZ_RIGHTOVARY')
                    '3dfz_avc_slice_b':'3DFZ_AVC_SLICE_B',			#显示卵泡3D的B视图	client.adjust_param('3DFZ_AVC_SLICE_B')
                    '3dfz_avc_slice_3d':'3DFZ_AVC_SLICE_3D',			#显示卵泡3D的3D图像	client.adjust_param('3DFZ_AVC_SLICE_3D')
                    '3dfz_avc_slice_c':'3DFZ_AVC_SLICE_C',			#显示卵泡3D的C视图	client.adjust_param('3DFZ_AVC_SLICE_C')
                    '3dfz_avc_slice_a':'3DFZ_AVC_SLICE_A',			#显示卵泡3D的A视图	client.adjust_param('3DFZ_AVC_SLICE_A')
                    '3dfz_ms_thlow_down':'3DFZ_MS_THLOW_DOWN',			#减小3D低回声阈值	client.adjust_param('3DFZ_MS_THLOW_DOWN')
                    '3dfz_ms_thlow_up':'3DFZ_MS_THLOW_UP',			#增大3D低回声阈值	client.adjust_param('3DFZ_MS_THLOW_UP')
                    '3dfz_ms_brightness_down':'3DFZ_MS_BRIGHTNESS_DOWN',			#减小3D卵泡亮度	client.adjust_param('3DFZ_MS_BRIGHTNESS_DOWN')
                    '3dfz_ms_brightness_up':'3DFZ_MS_BRIGHTNESS_UP',			#增大3D卵泡亮度	client.adjust_param('3DFZ_MS_BRIGHTNESS_UP')
                    '3dfz_avc_volpre':'3DFZ_AVC_VOLPRE',			#返回3D预激活模式	client.adjust_param('3DFZ_AVC_VOLPRE')
                    '3dpa_label_stic':'3DPA_LABEL_STIC',			#开启STIC页签	client.adjust_param('3DPA_LABEL_STIC')
                    'sticpa_user_mode1/surface':'STICPA_USER_MODE1/Surface',			#开启STIC第一个用户模式	client.adjust_param('STICPA_USER_MODE1/Surface')
                    'sticpa_disp_full':'STICPA_DISP_FULL',			#STIC预激活单幅显示	client.adjust_param('STICPA_DISP_FULL')
                    'sticpa_disp_dual':'STICPA_DISP_DUAL',			#STIC预激活双幅显示	client.adjust_param('STICPA_DISP_DUAL')
                    'sticpa_disp_quad':'STICPA_DISP_QUAD',			#STIC预激活四幅显示	client.adjust_param('STICPA_DISP_QUAD')
                    'sticpa_focus_down':'STICPA_FOCUS_DOWN',			#减小STIC焦点位置	client.adjust_param('STICPA_FOCUS_DOWN')
                    'sticpa_focus_up':'STICPA_FOCUS_UP',			#增大STIC焦点位置	client.adjust_param('STICPA_FOCUS_UP')
                    'sticpa_acquisition_time_up':'STICPA_ACQUISITION_TIME_UP',			#增大STIC采集时间	client.adjust_param('STICPA_ACQUISITION_TIME_UP')
                    'sticpa_acquisition_time_down':'STICPA_ACQUISITION_TIME_DOWN',			#减小STIC采集时间	client.adjust_param('STICPA_ACQUISITION_TIME_DOWN')
                    'sticpa_sweep_angle_down':'STICPA_SWEEP_ANGLE_DOWN',			#减小STIC摆动角度	client.adjust_param('STICPA_SWEEP_ANGLE_DOWN')
                    'sticpa_sweep_angle_up':'STICPA_SWEEP_ANGLE_UP',			#增大STIC摆动角度	client.adjust_param('STICPA_SWEEP_ANGLE_UP')
                    'sticpa_start':'STICPA_START',			#开启STIC实时模式	client.adjust_param('STICPA_START')
                    'sticfz_label_3d4d':'STICFZ_LABEL_3D4D',			#进入3D/4D页签	client.adjust_param('STICFZ_LABEL_3D4D')
                    'sticfz_edit_roi':'STICFZ_EDIT_ROI',			#编辑ROI锁定STIC视图	client.adjust_param('STICFZ_EDIT_ROI')
                    'sticfz_inversion':'STICFZ_INVERSION',			#反转STIC成像	client.adjust_param('STICFZ_INVERSION')
                    'sticfz_rotate':'STICFZ_ROTATE',			#自由旋转STIC成像	client.adjust_param('STICFZ_ROTATE')
                    'sticfz_autoface':'STICFZ_AUTOFACE',			#STIC一键显脸	client.adjust_param('STICFZ_AUTOFACE')
                    'sticfz_autoplay':'STICFZ_AUTOPLAY',			#自动回放STIC	client.adjust_param('STICFZ_AUTOPLAY')
                    'sticfz_disp_full':'STICFZ_DISP_FULL',			#STIC实时单幅显示	client.adjust_param('STICFZ_DISP_FULL')
                    'sticfz_disp_dual':'STICFZ_DISP_DUAL',			#STIC实时双幅显示	client.adjust_param('STICFZ_DISP_DUAL')
                    'sticfz_disp_quad':'STICFZ_DISP_QUAD',			#STIC实时四幅显示	client.adjust_param('STICFZ_DISP_QUAD')
                    'sticfz_orient_0':'STICFZ_ORIENT_0',			#0度旋转STIC	client.adjust_param('STICFZ_ORIENT_0')
                    'sticfz_orient_90':'STICFZ_ORIENT_90',			#90度旋转STIC	client.adjust_param('STICFZ_ORIENT_90')
                    'sticfz_reset':'STICFZ_RESET',			#复位	client.adjust_param('STICFZ_RESET')
                    'sticfz_orient_270':'STICFZ_ORIENT_270',			#270度旋转STIC	client.adjust_param('STICFZ_ORIENT_270')
                    'sticfz_orient_180':'STICFZ_ORIENT_180',			#180度旋转STIC	client.adjust_param('STICFZ_ORIENT_180')
                    'sticfz_slice_b':'STICFZ_SLICE_B',			#选择STIC的B视图	client.adjust_param('STICFZ_SLICE_B')
                    'sticfz_slice_3d':'STICFZ_SLICE_3D',			#选择STIC图像	client.adjust_param('STICFZ_SLICE_3D')
                    'sticfz_slice_c':'STICFZ_SLICE_C',			#选择STIC的C视图	client.adjust_param('STICFZ_SLICE_C')
                    'sticfz_slice_a':'STICFZ_SLICE_A',			#选择STIC的A视图	client.adjust_param('STICFZ_SLICE_A')
                    'sticfz_render_surface':'STICFZ_RENDER_SURFACE',			#开启STIC表面成像渲染模式	client.adjust_param('STICFZ_RENDER_SURFACE')
                    'sticfz_threshold_down':'STICFZ_THRESHOLD_DOWN',			#减小STIC阈值	client.adjust_param('STICFZ_THRESHOLD_DOWN')
                    'sticfz_threshold_up':'STICFZ_THRESHOLD_UP',			#增大STIC阈值	client.adjust_param('STICFZ_THRESHOLD_UP')
                    'sticfz_contrast_down':'STICFZ_CONTRAST_DOWN',			#减小STIC的对比度	client.adjust_param('STICFZ_CONTRAST_DOWN')
                    'sticfz_contrast_up':'STICFZ_CONTRAST_UP',			#增大STIC的对比度	client.adjust_param('STICFZ_CONTRAST_UP')
                    'sticfz_transparency_down':'STICFZ_TRANSPARENCY_DOWN',			#减小STIC的透明度	client.adjust_param('STICFZ_TRANSPARENCY_DOWN')
                    'sticfz_transparency_up':'STICFZ_TRANSPARENCY_UP',			#增大STIC的透明度	client.adjust_param('STICFZ_TRANSPARENCY_UP')
                    'sticfz_brightness_down':'STICFZ_BRIGHTNESS_DOWN',			#减小STIC亮度	client.adjust_param('STICFZ_BRIGHTNESS_DOWN')
                    'sticfz_brightness_up':'STICFZ_BRIGHTNESS_UP',			#增大STIC亮度	client.adjust_param('STICFZ_BRIGHTNESS_UP')
                    'sticfz_smoothness_down':'STICFZ_SMOOTHNESS_DOWN',			#减小STIC平滑值	client.adjust_param('STICFZ_SMOOTHNESS_DOWN')
                    'sticfz_smoothness_up':'STICFZ_SMOOTHNESS_UP',			#增大STIC平滑值	client.adjust_param('STICFZ_SMOOTHNESS_UP')
                    'sticfz_2duscan_down':'STICFZ_2DUSCAN_DOWN',			#减小STIC的2D微米成像值	client.adjust_param('STICFZ_2DUSCAN_DOWN')
                    'sticfz_2duscan_up':'STICFZ_2DUSCAN_UP',			#增大STIC的2D微米成像值	client.adjust_param('STICFZ_2DUSCAN_UP')
                    'sticfz_3duscan_down':'STICFZ_3DUSCAN_DOWN',			#减小STIC的3D微米成像值	client.adjust_param('STICFZ_3DUSCAN_DOWN')
                    'sticfz_3duscan_up':'STICFZ_3DUSCAN_UP',			#增大STIC的3D微米成像值	client.adjust_param('STICFZ_3DUSCAN_UP')
                    'sticfz_3dchroma_down':'STICFZ_3DCHROMA_DOWN',			#减小STIC的3D伪彩值	client.adjust_param('STICFZ_3DCHROMA_DOWN')
                    'sticfz_3dchroma_up':'STICFZ_3DCHROMA_UP',			#增大STIC的3D伪彩值	client.adjust_param('STICFZ_3DCHROMA_UP')
                    'sticfz_bchroma_down':'STICFZ_BCHROMA_DOWN',			#减小STIC的B伪彩值	client.adjust_param('STICFZ_BCHROMA_DOWN')
                    'sticfz_bchroma_up':'STICFZ_BCHROMA_UP',			#增大STIC的B伪彩值	client.adjust_param('STICFZ_BCHROMA_UP')
                    'sticfz_label_cplane':'STICFZ_LABEL_CPLANE',			#开启STIC截面页签	client.adjust_param('STICFZ_LABEL_CPLANE')
                    'sticfz_cp_2duscan_down':'STICFZ_CP_2DUSCAN_DOWN',			#增大STIC截面2D微米成像	client.adjust_param('STICFZ_CP_2DUSCAN_DOWN')
                    'sticfz_cp_2duscan_up':'STICFZ_CP_2DUSCAN_UP',			#减小STIC截面2D微米成像	client.adjust_param('STICFZ_CP_2DUSCAN_UP')
                    'sticfz_render_grad_light':'STICFZ_RENDER_GRAD_LIGHT',			#开启STIC梯度亮度渲染模式	client.adjust_param('STICFZ_RENDER_GRAD_LIGHT')
                    'sticfz_render_skeleton':'STICFZ_RENDER_SKELETON',			#开启STIC骨骼成像渲染模式	client.adjust_param('STICFZ_RENDER_SKELETON')
                    'sticfz_skeleton_depth':'STICFZ_SKELETON_DEPTH',			#开启STIC骨骼深度成像	client.adjust_param('STICFZ_SKELETON_DEPTH')
                    'sticfz_skeleton':'STICFZ_SKELETON',			#开启STIC骨骼成像	client.adjust_param('STICFZ_SKELETON')
                    'sticfz_render_transp_min':'STICFZ_RENDER_TRANSP_MIN',			#开启STIC最小回声成像渲染模式	client.adjust_param('STICFZ_RENDER_TRANSP_MIN')
                    'sticfz_render_xray':'STICFZ_RENDER_XRAY',			#开启STIC的X-线成像渲染模式	client.adjust_param('STICFZ_RENDER_XRAY')
                    'sticfz_render_sdepth':'STICFZ_RENDER_SDEPTH',			#开启STIC深度成像渲染模式	client.adjust_param('STICFZ_RENDER_SDEPTH')
                    'sticfz_render_slive':'STICFZ_RENDER_SLIVE',			#开启STIC的S-Live渲染模式	client.adjust_param('STICFZ_RENDER_SLIVE')
                    'sticfz_light_pos_up':'STICFZ_LIGHT_POS_UP',			#增大STIC的灯光位置	client.adjust_param('STICFZ_LIGHT_POS_UP')
                    'sticfz_light_pos_down':'STICFZ_LIGHT_POS_DOWN',			#减小STIC的灯光位置	client.adjust_param('STICFZ_LIGHT_POS_DOWN')
                    'sticfz_slive_silhouette':'STICFZ_SLIVE_SILHOUETTE',			#开启STIC的S-Live Silhouette结构	client.adjust_param('STICFZ_SLIVE_SILHOUETTE')
                    'sticfz_edit_light':'STICFZ_EDIT_LIGHT',			#开启STIC调节灯光功能	client.adjust_param('STICFZ_EDIT_LIGHT')
                    'sticfz_slive':'STICFZ_SLIVE',			#开启STIC的S-Live结构	client.adjust_param('STICFZ_SLIVE')
                    'sticfz_label_view':'STICFZ_LABEL_VIEW',			#开启STIC的视图页签	client.adjust_param('STICFZ_LABEL_VIEW')
                    'sticfz_rotate_45':'STICFZ_ROTATE_45',			#45度自由旋转STIC成像	client.adjust_param('STICFZ_ROTATE_45')
                    'sticfz_rotate_90':'STICFZ_ROTATE_90',			#90度自由旋转STIC成像	client.adjust_param('STICFZ_ROTATE_90')
                    'sticfz_rotate_360':'STICFZ_ROTATE_360',			#360度自由旋转STIC成像	client.adjust_param('STICFZ_ROTATE_360')
                    'sticfz_rotate_270':'STICFZ_ROTATE_270',			#270度自由旋转STIC成像	client.adjust_param('STICFZ_ROTATE_270')
                    'sticfz_rotate_180':'STICFZ_ROTATE_180',			#180度自由旋转STIC成像	client.adjust_param('STICFZ_ROTATE_180')
                    'sticfz_rotate_0':'STICFZ_ROTATE_0',			#0度自由旋转STIC成像	client.adjust_param('STICFZ_ROTATE_0')
                    'sticfz_direction_top':'STICFZ_DIRECTION_TOP',			#STIC顶部视图	client.adjust_param('STICFZ_DIRECTION_TOP')
                    'sticfz_direction_left':'STICFZ_DIRECTION_LEFT',			#STIC左侧视图	client.adjust_param('STICFZ_DIRECTION_LEFT')
                    'sticfz_direction_fornt':'STICFZ_DIRECTION_FORNT',			#STIC前面视图	client.adjust_param('STICFZ_DIRECTION_FORNT')
                    'sticfz_direction_back':'STICFZ_DIRECTION_BACK',			#STIC底部视图	client.adjust_param('STICFZ_DIRECTION_BACK')
                    'sticfz_direction_right':'STICFZ_DIRECTION_RIGHT',			#STIC右侧视图	client.adjust_param('STICFZ_DIRECTION_RIGHT')
                    'sticfz_direction_bottom':'STICFZ_DIRECTION_BOTTOM',			#STIC底部视图	client.adjust_param('STICFZ_DIRECTION_BOTTOM')
                    'sticfz_rotatex_up':'STICFZ_ROTATEX_UP',			#增大STIC的X旋转角度	client.adjust_param('STICFZ_ROTATEX_UP')
                    'sticfz_rotatex_down':'STICFZ_ROTATEX_DOWN',			#减小STIC的X旋转角度	client.adjust_param('STICFZ_ROTATEX_DOWN')
                    'sticfz_rotatey_up':'STICFZ_ROTATEY_UP',			#增大STIC的Y旋转角度	client.adjust_param('STICFZ_ROTATEY_UP')
                    'sticfz_rotatey_down':'STICFZ_ROTATEY_DOWN',			#减小STIC的Y旋转角度	client.adjust_param('STICFZ_ROTATEY_DOWN')
                    'sticfz_rotatez_up':'STICFZ_ROTATEZ_UP',			#增大STIC的Z旋转角度	client.adjust_param('STICFZ_ROTATEZ_UP')
                    'sticfz_rotatez_down':'STICFZ_ROTATEZ_DOWN',			#减小STIC的Z旋转角度	client.adjust_param('STICFZ_ROTATEZ_DOWN')
                    'sticfz_moveud_up':'STICFZ_MOVEUD_UP',			#STIC向上移动	client.adjust_param('STICFZ_MOVEUD_UP')
                    'sticfz_moveud_down':'STICFZ_MOVEUD_DOWN',			#STIC向下移动	client.adjust_param('STICFZ_MOVEUD_DOWN')
                    'sticfz_movelr_up':'STICFZ_MOVELR_UP',			#STIC向右移动	client.adjust_param('STICFZ_MOVELR_UP')
                    'sticfz_movelr_down':'STICFZ_MOVELR_DOWN',			#STIC向左移动	client.adjust_param('STICFZ_MOVELR_DOWN')
                    'sticfz_edit_rotate':'STICFZ_EDIT_ROTATE',			#开启STIC编辑页签	client.adjust_param('STICFZ_EDIT_ROTATE')
                    'sticfz_cut_method1':'STICFZ_CUT_METHOD1',			#STIC描迹剪切区域内部分	client.adjust_param('STICFZ_CUT_METHOD1')
                    'sticfz_cut_method3':'STICFZ_CUT_METHOD3',			#STIC方框剪切区域内部分	client.adjust_param('STICFZ_CUT_METHOD3')
                    'sticfz_cut_method6':'STICFZ_CUT_METHOD6',			#STIC大橡皮擦剪切	client.adjust_param('STICFZ_CUT_METHOD6')
                    'sticfz_cut_method5':'STICFZ_CUT_METHOD5',			#STIC小橡皮擦剪切	client.adjust_param('STICFZ_CUT_METHOD5')
                    'sticfz_cut_method4':'STICFZ_CUT_METHOD4',			#STIC方框剪切区域外部分	client.adjust_param('STICFZ_CUT_METHOD4')
                    'sticfz_cut_method2':'STICFZ_CUT_METHOD2',			#STIC描迹剪切区域外部分	client.adjust_param('STICFZ_CUT_METHOD2')
                    'sticfz_disp_ab':'STICFZ_DISP_AB',			#STIC显示AB视图	client.adjust_param('STICFZ_DISP_AB')
                    'sticfz_cp_slice_b':'STICFZ_CP_SLICE_B',			#STIC选择B视图进行层切	client.adjust_param('STICFZ_CP_SLICE_B')
                    'sticfz_cp_slice_a':'STICFZ_CP_SLICE_A',			#STIC选择A视图进行层切	client.adjust_param('STICFZ_CP_SLICE_A')
                    'sticfz_disp_ac':'STICFZ_DISP_AC',			#STIC显示AC视图	client.adjust_param('STICFZ_DISP_AC')
                    'sticfz_cp_slice_c':'STICFZ_CP_SLICE_C',			#STIC选择C视图进行层切	client.adjust_param('STICFZ_CP_SLICE_C')
                    'sticfz_disp_bc':'STICFZ_DISP_BC',			#STIC显示BC视图	client.adjust_param('STICFZ_DISP_BC')
                    'sticfz_disp_abc':'STICFZ_DISP_ABC',			#STIC显示ABC视图	client.adjust_param('STICFZ_DISP_ABC')
                    'sticfz_cp_bchroma_down':'STICFZ_CP_BCHROMA_DOWN',			#减小STIC的B伪彩值	client.adjust_param('STICFZ_CP_BCHROMA_DOWN')
                    'sticfz_cp_bchroma_up':'STICFZ_CP_BCHROMA_UP',			#增大STIC的B伪彩值	client.adjust_param('STICFZ_CP_BCHROMA_UP')
                    'sticfz_label_mslice':'STICFZ_LABEL_MSLICE',			#开启STIC断层切片页签	client.adjust_param('STICFZ_LABEL_MSLICE')
                    'sticfz_ms_slice_b':'STICFZ_MS_SLICE_B',			#选择STIC的B切片平面	client.adjust_param('STICFZ_MS_SLICE_B')
                    'sticfz_ms_slice_c':'STICFZ_MS_SLICE_C',			#选择STIC的C切片平面	client.adjust_param('STICFZ_MS_SLICE_C')
                    'sticfz_ms_slice_a':'STICFZ_MS_SLICE_A',			#选择STIC的A切片平面	client.adjust_param('STICFZ_MS_SLICE_A')
                    'sticfz_disp_12':'STICFZ_DISP_12',			#设置STIC显示模式为1*2	client.adjust_param('STICFZ_DISP_12')
                    'sticfz_disp_33':'STICFZ_DISP_33',			#设置STIC显示模式为3*3	client.adjust_param('STICFZ_DISP_33')
                    'sticfz_disp_44':'STICFZ_DISP_44',			#设置STIC显示模式为4*4	client.adjust_param('STICFZ_DISP_44')
                    'sticfz_disp_55':'STICFZ_DISP_55',			#设置STIC显示模式为2*2	client.adjust_param('STICFZ_DISP_55')
                    'sticfz_disp_34':'STICFZ_DISP_34',			#设置STIC显示模式为3*4	client.adjust_param('STICFZ_DISP_34')
                    'sticfz_disp_22':'STICFZ_DISP_22',			#设置STIC显示模式为2*2	client.adjust_param('STICFZ_DISP_22')
                    'sticfz_ms_bchroma_up':'STICFZ_MS_BCHROMA_UP',			#增大STIC断层切片的B伪彩值	client.adjust_param('STICFZ_MS_BCHROMA_UP')
                    'sticfz_ms_bchroma_down':'STICFZ_MS_BCHROMA_DOWN',			#减小STIC断层切片的B伪彩值	client.adjust_param('STICFZ_MS_BCHROMA_DOWN')
                    'sticfz_ms_adjustpos_up':'STICFZ_MS_ADJUSTPOS_UP',			#微增大STIC所选切片的位置	client.adjust_param('STICFZ_MS_ADJUSTPOS_UP')
                    'sticfz_ms_adjustpos_down':'STICFZ_MS_ADJUSTPOS_DOWN',			#微减小STIC所选切片的位置	client.adjust_param('STICFZ_MS_ADJUSTPOS_DOWN')
                    'sticfz_ms_distance_up':'STICFZ_MS_DISTANCE_UP',			#增大STIC切片间距	client.adjust_param('STICFZ_MS_DISTANCE_UP')
                    'sticfz_ms_distance_down':'STICFZ_MS_DISTANCE_DOWN',			#减小STIC切片间距	client.adjust_param('STICFZ_MS_DISTANCE_DOWN')
                    'sticfz_ms_slicenum_down':'STICFZ_MS_SLICENUM_DOWN',			#减少STIC切片数量	client.adjust_param('STICFZ_MS_SLICENUM_DOWN')
                    'sticfz_ms_slicenum_up':'STICFZ_MS_SLICENUM_UP',			#增多STIC切片数量	client.adjust_param('STICFZ_MS_SLICENUM_UP')
                    'sticfz_ms_display_up':'STICFZ_MS_DISPLAY_UP',			#向右平移STIC切片区域所有切片	client.adjust_param('STICFZ_MS_DISPLAY_UP')
                    'sticfz_ms_display_down':'STICFZ_MS_DISPLAY_DOWN',			#向左平移STIC切片区域所有切片	client.adjust_param('STICFZ_MS_DISPLAY_DOWN')
                    'sticfz_volpre':'STICFZ_VOLPRE',			#返回STIC预激活模式	client.adjust_param('STICFZ_VOLPRE')
                    '3d_menu_exit':'3D_MENU_EXIT',			#退出3D/4D模式	client.adjust_param('3D_MENU_EXIT')
                    # CFM-3D4D
                    'cfm3dpa_user_mode1':'CFM3DPA_USER_MODE1',			#开启3D第一个用户模式	client.adjust_param('CFM3DPA_USER_MODE1')
                    'cfm3dpa_user_mode2':'CFM3DPA_USER_MODE2',			#开启3D第二个用户模式	client.adjust_param('CFM3DPA_USER_MODE2')
                    'cfm3dpa_user_mode3':'CFM3DPA_USER_MODE3',			#开启3D第三个用户模式	client.adjust_param('CFM3DPA_USER_MODE3')
                    'cfm3dpa_disp_full':'CFM3DPA_DISP_FULL',			#3D预激活单幅显示	client.adjust_param('CFM3DPA_DISP_FULL')
                    'cfm3dpa_disp_dual':'CFM3DPA_DISP_DUAL',			#3D预激活双幅显示	client.adjust_param('CFM3DPA_DISP_DUAL')
                    'cfm3dpa_disp_quad':'CFM3DPA_DISP_QUAD',			#3D预激活四幅显示	client.adjust_param('CFM3DPA_DISP_QUAD')
                    'cfm3dpa_image_quality_up':'CFM3DPA_IMAGE_QUALITY_UP',			#增大3D图像质量	client.adjust_param('CFM3DPA_IMAGE_QUALITY_UP')
                    'cfm3dpa_image_quality_down':'CFM3DPA_IMAGE_QUALITY_DOWN',			#减小3D图像质量	client.adjust_param('CFM3DPA_IMAGE_QUALITY_DOWN')
                    'cfm3dpa_sweep_angle_up':'CFM3DPA_SWEEP_ANGLE_UP',			#增大3D摆动角度	client.adjust_param('CFM3DPA_SWEEP_ANGLE_UP')
                    'cfm3dpa_sweep_angle_down':'CFM3DPA_SWEEP_ANGLE_DOWN',			#减小3D摆动角度	client.adjust_param('CFM3DPA_SWEEP_ANGLE_DOWN')
                    'cfm3dpa_start':'CFM3DPA_START',			#开启3D实时模式	client.adjust_param('CFM3DPA_START')
                    'cfm3dfz_label_3d4d':'CFM3DFZ_LABEL_3D4D',			#进入3D/4D页签	client.adjust_param('CFM3DFZ_LABEL_3D4D')
                    'cfm3dfz_edit_roi':'CFM3DFZ_EDIT_ROI',			#编辑ROI锁定3D视图	client.adjust_param('CFM3DFZ_EDIT_ROI')
                    'cfm3dfz_rotate':'CFM3DFZ_ROTATE',			#反转3D成像	client.adjust_param('CFM3DFZ_ROTATE')
                    'cfm3dfz_color_off':'CFM3DFZ_COLOR_OFF',			#关闭3D血流	client.adjust_param('CFM3DFZ_COLOR_OFF')
                    'cfm3dfz_disp_full':'CFM3DFZ_DISP_FULL',			#3D实时单幅显示	client.adjust_param('CFM3DFZ_DISP_FULL')
                    'cfm3dfz_disp_dual':'CFM3DFZ_DISP_DUAL',			#3D实时双幅显示	client.adjust_param('CFM3DFZ_DISP_DUAL')
                    'cfm3dfz_disp_quad':'CFM3DFZ_DISP_QUAD',			#3D实时四幅显示	client.adjust_param('CFM3DFZ_DISP_QUAD')
                    'cfm3dfz_orient_90':'CFM3DFZ_ORIENT_90',			#90度旋转3D	client.adjust_param('CFM3DFZ_ORIENT_90')
                    'cfm3dfz_orient_270':'CFM3DFZ_ORIENT_270',			#270度旋转3D	client.adjust_param('CFM3DFZ_ORIENT_270')
                    'cfm3dfz_reset':'CFM3DFZ_RESET',			#复位3D	client.adjust_param('CFM3DFZ_RESET')
                    'cfm3dfz_orient_0':'CFM3DFZ_ORIENT_0',			#0度旋转3D	client.adjust_param('CFM3DFZ_ORIENT_0')
                    'cfm3dfz_orient_180':'CFM3DFZ_ORIENT_180',			#180度旋转3D	client.adjust_param('CFM3DFZ_ORIENT_180')
                    'cfm3dfz_slice_b':'CFM3DFZ_SLICE_B',			#选择3D的B视图	client.adjust_param('CFM3DFZ_SLICE_B')
                    'cfm3dfz_slice_3d':'CFM3DFZ_SLICE_3D',			#选择3D图像	client.adjust_param('CFM3DFZ_SLICE_3D')
                    'cfm3dfz_slice_c':'CFM3DFZ_SLICE_C',			#选择3D的C视图	client.adjust_param('CFM3DFZ_SLICE_C')
                    'cfm3dfz_slice_a':'CFM3DFZ_SLICE_A',			#选择3D的A视图	client.adjust_param('CFM3DFZ_SLICE_A')
                    'cfm3dfz_render_color_surface':'CFM3DFZ_RENDER_COLOR_SURFACE',			#开启3D血流表面成像渲染模式	client.adjust_param('CFM3DFZ_RENDER_COLOR_SURFACE')
                    'cfm3dfz_color_threshold_up':'CFM3DFZ_COLOR_THRESHOLD_UP',			#增大3D血流阈值	client.adjust_param('CFM3DFZ_COLOR_THRESHOLD_UP')
                    'cfm3dfz_color_threshold_down':'CFM3DFZ_COLOR_THRESHOLD_DOWN',			#减小3D血流阈值	client.adjust_param('CFM3DFZ_COLOR_THRESHOLD_DOWN')
                    'cfm3dfz_transparency_up':'CFM3DFZ_TRANSPARENCY_UP',			#增大3D的透明度	client.adjust_param('CFM3DFZ_TRANSPARENCY_UP')
                    'cfm3dfz_transparency_down':'CFM3DFZ_TRANSPARENCY_DOWN',			#减小3D的透明度	client.adjust_param('CFM3DFZ_TRANSPARENCY_DOWN')
                    'cfm3dfz_brightness_up':'CFM3DFZ_BRIGHTNESS_UP',			#增大3D亮度	client.adjust_param('CFM3DFZ_BRIGHTNESS_UP')
                    'cfm3dfz_brightness_down':'CFM3DFZ_BRIGHTNESS_DOWN',			#减小3D亮度	client.adjust_param('CFM3DFZ_BRIGHTNESS_DOWN')
                    'cfm3dfz_smoothness_up':'CFM3DFZ_SMOOTHNESS_UP',			#增大3D平滑值	client.adjust_param('CFM3DFZ_SMOOTHNESS_UP')
                    'cfm3dfz_smoothness_down':'CFM3DFZ_SMOOTHNESS_DOWN',			#减小3D平滑值	client.adjust_param('CFM3DFZ_SMOOTHNESS_DOWN')
                    'cfm3dfz_color_chroma_up':'CFM3DFZ_COLOR_CHROMA_UP',			#增大3D彩色图谱值	client.adjust_param('CFM3DFZ_COLOR_CHROMA_UP')
                    'cfm3dfz_color_chroma_down':'CFM3DFZ_COLOR_CHROMA_DOWN',			#减小3D彩色图谱值	client.adjust_param('CFM3DFZ_COLOR_CHROMA_DOWN')
                    'cfm3dfz_bchroma_up':'CFM3DFZ_BCHROMA_UP',			#增大3D的B伪彩值	client.adjust_param('CFM3DFZ_BCHROMA_UP')
                    'cfm3dfz_bchroma_down':'CFM3DFZ_BCHROMA_DOWN',			#减小3D的B伪彩值	client.adjust_param('CFM3DFZ_BCHROMA_DOWN')
                    'cfm3dfz_render_color_xray':'CFM3DFZ_RENDER_COLOR_XRAY',			#开启3D的X-线成像渲染模式	client.adjust_param('CFM3DFZ_RENDER_COLOR_XRAY')
                    'cfm3dfz_render_glass_surface':'CFM3DFZ_RENDER_GLASS_SURFACE',			#开启3D的表面+表面成像渲染模式	client.adjust_param('CFM3DFZ_RENDER_GLASS_SURFACE')
                    'cfm3dfz_color_color_ratio_down':'CFM3DFZ_COLOR_COLOR_RATIO_DOWN',			#减小3D的灰度/血流值	client.adjust_param('CFM3DFZ_COLOR_COLOR_RATIO_DOWN')
                    'cfm3dfz_color_color_ratio_up':'CFM3DFZ_COLOR_COLOR_RATIO_UP',			#增大3D的灰度/血流值	client.adjust_param('CFM3DFZ_COLOR_COLOR_RATIO_UP')
                    'cfm3dfz_contrast_down':'CFM3DFZ_CONTRAST_DOWN',			#减小3D的对比度	client.adjust_param('CFM3DFZ_CONTRAST_DOWN')
                    'cfm3dfz_contrast_up':'CFM3DFZ_CONTRAST_UP',			#增大3D的对比度	client.adjust_param('CFM3DFZ_CONTRAST_UP')
                    'cfm3dfz_threshold_down':'CFM3DFZ_THRESHOLD_DOWN',			#减小3D阈值	client.adjust_param('CFM3DFZ_THRESHOLD_DOWN')
                    'cfm3dfz_threshold_up':'CFM3DFZ_THRESHOLD_UP',			#增大3D阈值	client.adjust_param('CFM3DFZ_THRESHOLD_UP')
                    'cfm3dfz_3dchroma_down':'CFM3DFZ_3DCHROMA_DOWN',			#减小3D的3D伪彩值	client.adjust_param('CFM3DFZ_3DCHROMA_DOWN')
                    'cfm3dfz_3dchroma_up':'CFM3DFZ_3DCHROMA_UP',			#增大3D的3D伪彩值	client.adjust_param('CFM3DFZ_3DCHROMA_UP')
                    'cfm3dfz_render_surface':'CFM3DFZ_RENDER_SURFACE',			#开启3D表面成像渲染模式	client.adjust_param('CFM3DFZ_RENDER_SURFACE')
                    'cfm3dfz_render_color_maxip':'CFM3DFZ_RENDER_COLOR_MAXIP',			#开启3D最大密度渲染模式	client.adjust_param('CFM3DFZ_RENDER_COLOR_MAXIP')
                    'cfm3dfz_render_color_grad_light':'CFM3DFZ_RENDER_COLOR_GRAD_LIGHT',			#开启3D血流梯度亮度渲染模式	client.adjust_param('CFM3DFZ_RENDER_COLOR_GRAD_LIGHT')
                    'cfm3dfz_render_glass_surface_maxip':'CFM3DFZ_RENDER_GLASS_SURFACE_MAXIP',			#开启3D表面+最大密度渲染模式	client.adjust_param('CFM3DFZ_RENDER_GLASS_SURFACE_MAXIP')
                    'cfm3dfz_render_grad_light':'CFM3DFZ_RENDER_GRAD_LIGHT',			#开启3D梯度亮度渲染模式	client.adjust_param('CFM3DFZ_RENDER_GRAD_LIGHT')
                    'cfm3dfz_label_view':'CFM3DFZ_LABEL_VIEW',			#开启3D的视图页签	client.adjust_param('CFM3DFZ_LABEL_VIEW')
                    'cfm3dfz_rotate_45':'CFM3DFZ_ROTATE_45',			#45度自由旋转3D成像	client.adjust_param('CFM3DFZ_ROTATE_45')
                    'cfm3dfz_rotate_90':'CFM3DFZ_ROTATE_90',			#90度自由旋转3D成像	client.adjust_param('CFM3DFZ_ROTATE_90')
                    'cfm3dfz_rotate_360':'CFM3DFZ_ROTATE_360',			#360度自由旋转3D成像	client.adjust_param('CFM3DFZ_ROTATE_360')
                    'cfm3dfz_rotate_270':'CFM3DFZ_ROTATE_270',			#270度自由旋转3D成像	client.adjust_param('CFM3DFZ_ROTATE_270')
                    'cfm3dfz_rotate_180':'CFM3DFZ_ROTATE_180',			#180度自由旋转3D成像	client.adjust_param('CFM3DFZ_ROTATE_180')
                    'cfm3dfz_rotate_0':'CFM3DFZ_ROTATE_0',			#0度自由旋转3D成像	client.adjust_param('CFM3DFZ_ROTATE_0')
                    'cfm3dfz_direction_bottom':'CFM3DFZ_DIRECTION_BOTTOM',			#3D底部视图	client.adjust_param('CFM3DFZ_DIRECTION_BOTTOM')
                    'cfm3dfz_direction_top':'CFM3DFZ_DIRECTION_TOP',			#3D顶部视图	client.adjust_param('CFM3DFZ_DIRECTION_TOP')
                    'cfm3dfz_direction_left':'CFM3DFZ_DIRECTION_LEFT',			#3D左侧视图	client.adjust_param('CFM3DFZ_DIRECTION_LEFT')
                    'cfm3dfz_direction_right':'CFM3DFZ_DIRECTION_RIGHT',			#3D右侧视图	client.adjust_param('CFM3DFZ_DIRECTION_RIGHT')
                    'cfm3dfz_direction_fornt':'CFM3DFZ_DIRECTION_FORNT',			#3D前面视图	client.adjust_param('CFM3DFZ_DIRECTION_FORNT')
                    'cfm3dfz_direction_back':'CFM3DFZ_DIRECTION_BACK',			#3D后面视图	client.adjust_param('CFM3DFZ_DIRECTION_BACK')
                    'cfm3dfz_rotatex_up':'CFM3DFZ_ROTATEX_UP',			#增大3D的X旋转角度	client.adjust_param('CFM3DFZ_ROTATEX_UP')
                    'cfm3dfz_rotatex_down':'CFM3DFZ_ROTATEX_DOWN',			#减小3D的X旋转角度	client.adjust_param('CFM3DFZ_ROTATEX_DOWN')
                    'cfm3dfz_rotatey_up':'CFM3DFZ_ROTATEY_UP',			#增大3D的Y旋转角度	client.adjust_param('CFM3DFZ_ROTATEY_UP')
                    'cfm3dfz_rotatey_down':'CFM3DFZ_ROTATEY_DOWN',			#减小3D的Y旋转角度	client.adjust_param('CFM3DFZ_ROTATEY_DOWN')
                    'cfm3dfz_rotatez_up':'CFM3DFZ_ROTATEZ_UP',			#增大3D的Z旋转角度	client.adjust_param('CFM3DFZ_ROTATEZ_UP')
                    'cfm3dfz_rotatez_down':'CFM3DFZ_ROTATEZ_DOWN',			#减小3D的Z旋转角度	client.adjust_param('CFM3DFZ_ROTATEZ_DOWN')
                    'cfm3dfz_moveud_up':'CFM3DFZ_MOVEUD_UP',			#3D向上移动	client.adjust_param('CFM3DFZ_MOVEUD_UP')
                    'cfm3dfz_moveud_down':'CFM3DFZ_MOVEUD_DOWN',			#3D向下移动	client.adjust_param('CFM3DFZ_MOVEUD_DOWN')
                    'cfm3dfz_movelr_up':'CFM3DFZ_MOVELR_UP',			#3D向右移动	client.adjust_param('CFM3DFZ_MOVELR_UP')
                    'cfm3dfz_movelr_down':'CFM3DFZ_MOVELR_DOWN',			#3D向左移动	client.adjust_param('CFM3DFZ_MOVELR_DOWN')
                    'cfm3dfz_label_edit':'CFM3DFZ_LABEL_EDIT',			#开启3D编辑页签	client.adjust_param('CFM3DFZ_LABEL_EDIT')
                    'cfm3dfz_edit_rotate':'CFM3DFZ_EDIT_ROTATE',			#自由旋转3D成像	client.adjust_param('CFM3DFZ_EDIT_ROTATE')
                    'cfm3dfz_cut_method3':'CFM3DFZ_CUT_METHOD3',			#3D方框剪切区域内部分	client.adjust_param('CFM3DFZ_CUT_METHOD3')
                    'cfm3dfz_cut_method6':'CFM3DFZ_CUT_METHOD6',			#3D大橡皮擦剪切	client.adjust_param('CFM3DFZ_CUT_METHOD6')
                    'cfm3dfz_cut_method5':'CFM3DFZ_CUT_METHOD5',			#3D小橡皮擦剪切	client.adjust_param('CFM3DFZ_CUT_METHOD5')
                    'cfm3dfz_cut_method4':'CFM3DFZ_CUT_METHOD4',			#3D方框剪切区域外部分	client.adjust_param('CFM3DFZ_CUT_METHOD4')
                    'cfm3dfz_cut_method2':'CFM3DFZ_CUT_METHOD2',			#3D描迹剪切区域外部分	client.adjust_param('CFM3DFZ_CUT_METHOD2')
                    'cfm3dfz_cut_method1':'CFM3DFZ_CUT_METHOD1',			#3D描迹剪切区域内部分	client.adjust_param('CFM3DFZ_CUT_METHOD1')
                    'cfm3dfz_label_cplane':'CFM3DFZ_LABEL_CPLANE',			#开启3D截面页签	client.adjust_param('CFM3DFZ_LABEL_CPLANE')
                    'cfm3dfz_disp_ab':'CFM3DFZ_DISP_AB',			#显示3D的AB视图	client.adjust_param('CFM3DFZ_DISP_AB')
                    'cfm3dfz_cp_slice_b':'CFM3DFZ_CP_SLICE_B',			#选择3D的B视图进行层切	client.adjust_param('CFM3DFZ_CP_SLICE_B')
                    'cfm3dfz_cp_slice_a':'CFM3DFZ_CP_SLICE_A',			#选择3D的A视图进行层切	client.adjust_param('CFM3DFZ_CP_SLICE_A')
                    'cfm3dfz_disp_ac':'CFM3DFZ_DISP_AC',			#显示3D的AC视图	client.adjust_param('CFM3DFZ_DISP_AC')
                    'cfm3dfz_cp_slice_c':'CFM3DFZ_CP_SLICE_C',			#选择3D的C视图进行层切	client.adjust_param('CFM3DFZ_CP_SLICE_C')
                    'cfm3dfz_disp_bc':'CFM3DFZ_DISP_BC',			#显示3D的BC视图	client.adjust_param('CFM3DFZ_DISP_BC')
                    'cfm3dfz_disp_abc':'CFM3DFZ_DISP_ABC',			#显示3D的ABC视图	client.adjust_param('CFM3DFZ_DISP_ABC')
                    'cfm3dfz_cp_bchroma_up':'CFM3DFZ_CP_BCHROMA_UP',			#增大3D的B伪彩值	client.adjust_param('CFM3DFZ_CP_BCHROMA_UP')
                    'cfm3dfz_cp_bchroma_down':'CFM3DFZ_CP_BCHROMA_DOWN',			#减小3D的B伪彩值	client.adjust_param('CFM3DFZ_CP_BCHROMA_DOWN')
                    'cfm3dfz_label_mslice':'CFM3DFZ_LABEL_MSLICE',			#开启3D的断层切片页签	client.adjust_param('CFM3DFZ_LABEL_MSLICE')
                    'cfm3dfz_ms_slice_b':'CFM3DFZ_MS_SLICE_B',			#选择3D的B切片平面	client.adjust_param('CFM3DFZ_MS_SLICE_B')
                    'cfm3dfz_ms_slice_c':'CFM3DFZ_MS_SLICE_C',			#选择3D的C切片平面	client.adjust_param('CFM3DFZ_MS_SLICE_C')
                    'cfm3dfz_ms_slice_a':'CFM3DFZ_MS_SLICE_A',			#选择3D的A切片平面	client.adjust_param('CFM3DFZ_MS_SLICE_A')
                    'cfm3dfz_disp_12':'CFM3DFZ_DISP_12',			#设置3D显示模式为1*2	client.adjust_param('CFM3DFZ_DISP_12')
                    'cfm3dfz_disp_33':'CFM3DFZ_DISP_33',			#设置3D显示模式为3*3	client.adjust_param('CFM3DFZ_DISP_33')
                    'cfm3dfz_disp_44':'CFM3DFZ_DISP_44',			#设置3D显示模式为4*4	client.adjust_param('CFM3DFZ_DISP_44')
                    'cfm3dfz_disp_55':'CFM3DFZ_DISP_55',			#设置3D显示模式为5*5	client.adjust_param('CFM3DFZ_DISP_55')
                    'cfm3dfz_disp_34':'CFM3DFZ_DISP_34',			#设置3D显示模式为3*4	client.adjust_param('CFM3DFZ_DISP_34')
                    'cfm3dfz_disp_22':'CFM3DFZ_DISP_22',			#设置3D显示模式为2*2	client.adjust_param('CFM3DFZ_DISP_22')
                    'cfm3dfz_ms_bchroma_up':'CFM3DFZ_MS_BCHROMA_UP',			#增大3D断层切片的B伪彩值	client.adjust_param('CFM3DFZ_MS_BCHROMA_UP')
                    'cfm3dfz_ms_bchroma_down':'CFM3DFZ_MS_BCHROMA_DOWN',			#减小3D断层切片的B伪彩值	client.adjust_param('CFM3DFZ_MS_BCHROMA_DOWN')
                    'cfm3dfz_ms_adjustpos_up':'CFM3DFZ_MS_ADJUSTPOS_UP',			#微增大3D所选切片的位置	client.adjust_param('CFM3DFZ_MS_ADJUSTPOS_UP')
                    'cfm3dfz_ms_adjustpos_down':'CFM3DFZ_MS_ADJUSTPOS_DOWN',			#微减小3D所选切片的位置	client.adjust_param('CFM3DFZ_MS_ADJUSTPOS_DOWN')
                    'cfm3dfz_ms_distance_up':'CFM3DFZ_MS_DISTANCE_UP',			#增大3D切片间距	client.adjust_param('CFM3DFZ_MS_DISTANCE_UP')
                    'cfm3dfz_ms_distance_down':'CFM3DFZ_MS_DISTANCE_DOWN',			#减小3D切片间距	client.adjust_param('CFM3DFZ_MS_DISTANCE_DOWN')
                    'cfm3dfz_ms_slicenum_up':'CFM3DFZ_MS_SLICENUM_UP',			#增多3D切片数量	client.adjust_param('CFM3DFZ_MS_SLICENUM_UP')
                    'cfm3dfz_ms_slicenum_down':'CFM3DFZ_MS_SLICENUM_DOWN',			#减少3D切片数量	client.adjust_param('CFM3DFZ_MS_SLICENUM_DOWN')
                    'cfm3dfz_ms_display_up':'CFM3DFZ_MS_DISPLAY_UP',			#向左平移3D切片区域所有切片	client.adjust_param('CFM3DFZ_MS_DISPLAY_UP')
                    'cfm3dfz_ms_display_down':'CFM3DFZ_MS_DISPLAY_DOWN',			#向右平移3D切片区域所有切片	client.adjust_param('CFM3DFZ_MS_DISPLAY_DOWN')
                    'cfm3dfz_volpre':'CFM3DFZ_VOLPRE',			#返回3D预激活模式	client.adjust_param('CFM3DFZ_VOLPRE')
                    # PDI-3D4D
                    'pdi3dpa_user_mode1':'PDI3DPA_USER_MODE1',			#开启3D第一个用户模式	client.adjust_param('PDI3DPA_USER_MODE1')
                    'pdi3dpa_user_mode2':'PDI3DPA_USER_MODE2',			#开启3D第二个用户模式	client.adjust_param('PDI3DPA_USER_MODE2')
                    'pdi3dpa_user_mode3':'PDI3DPA_USER_MODE3',			#开启3D第三个用户模式	client.adjust_param('PDI3DPA_USER_MODE3')
                    'pdi3dpa_disp_full':'PDI3DPA_DISP_FULL',			#3D预激活单幅显示	client.adjust_param('PDI3DPA_DISP_FULL')
                    'pdi3dpa_disp_dual':'PDI3DPA_DISP_DUAL',			#3D预激活双幅显示	client.adjust_param('PDI3DPA_DISP_DUAL')
                    'pdi3dpa_disp_quad':'PDI3DPA_DISP_QUAD',			#3D预激活四幅显示	client.adjust_param('PDI3DPA_DISP_QUAD')
                    'pdi3dpa_image_quality_up':'PDI3DPA_IMAGE_QUALITY_UP',			#增大3D图像质量	client.adjust_param('PDI3DPA_IMAGE_QUALITY_UP')
                    'pdi3dpa_image_quality_down':'PDI3DPA_IMAGE_QUALITY_DOWN',			#减小3D图像质量	client.adjust_param('PDI3DPA_IMAGE_QUALITY_DOWN')
                    'pdi3dpa_sweep_angle_up':'PDI3DPA_SWEEP_ANGLE_UP',			#增大3D摆动角度	client.adjust_param('PDI3DPA_SWEEP_ANGLE_UP')
                    'pdi3dpa_sweep_angle_down':'PDI3DPA_SWEEP_ANGLE_DOWN',			#减小3D摆动角度	client.adjust_param('PDI3DPA_SWEEP_ANGLE_DOWN')
                    'pdi3dpa_start':'PDI3DPA_START',			#开启3D实时模式	client.adjust_param('PDI3DPA_START')
                    'pdi3dfz_label_3d4d':'PDI3DFZ_LABEL_3D4D',			#进入3D/4D页签	client.adjust_param('PDI3DFZ_LABEL_3D4D')
                    'pdi3dfz_edit_roi':'PDI3DFZ_EDIT_ROI',			#编辑ROI锁定3D视图	client.adjust_param('PDI3DFZ_EDIT_ROI')
                    'pdi3dfz_rotate':'PDI3DFZ_ROTATE',			#反转3D成像	client.adjust_param('PDI3DFZ_ROTATE')
                    'pdi3dfz_color_off':'PDI3DFZ_COLOR_OFF',			#关闭3D血流	client.adjust_param('PDI3DFZ_COLOR_OFF')
                    'pdi3dfz_disp_full':'PDI3DFZ_DISP_FULL',			#3D实时单幅显示	client.adjust_param('PDI3DFZ_DISP_FULL')
                    'pdi3dfz_disp_dual':'PDI3DFZ_DISP_DUAL',			#3D实时双幅显示	client.adjust_param('PDI3DFZ_DISP_DUAL')
                    'pdi3dfz_disp_quad':'PDI3DFZ_DISP_QUAD',			#3D实时四幅显示	client.adjust_param('PDI3DFZ_DISP_QUAD')
                    'pdi3dfz_orient_90':'PDI3DFZ_ORIENT_90',			#90度旋转3D	client.adjust_param('PDI3DFZ_ORIENT_90')
                    'pdi3dfz_orient_270':'PDI3DFZ_ORIENT_270',			#270度旋转3D	client.adjust_param('PDI3DFZ_ORIENT_270')
                    'pdi3dfz_reset':'PDI3DFZ_RESET',			#复位3D	client.adjust_param('PDI3DFZ_RESET')
                    'pdi3dfz_orient_180':'PDI3DFZ_ORIENT_180',			#180度旋转3D	client.adjust_param('PDI3DFZ_ORIENT_180')
                    'pdi3dfz_orient_0':'PDI3DFZ_ORIENT_0',			#0度旋转3D	client.adjust_param('PDI3DFZ_ORIENT_0')
                    'pdi3dfz_slice_b':'PDI3DFZ_SLICE_B',			#选择3D的B视图	client.adjust_param('PDI3DFZ_SLICE_B')
                    'pdi3dfz_slice_3d':'PDI3DFZ_SLICE_3D',			#选择3D图像	client.adjust_param('PDI3DFZ_SLICE_3D')
                    'pdi3dfz_slice_c':'PDI3DFZ_SLICE_C',			#选择3D的C视图	client.adjust_param('PDI3DFZ_SLICE_C')
                    'pdi3dfz_slice_a':'PDI3DFZ_SLICE_A',			#选择3D的A视图	client.adjust_param('PDI3DFZ_SLICE_A')
                    'pdi3dfz_render_color_surface':'PDI3DFZ_RENDER_COLOR_SURFACE',			#开启3D血流表面成像渲染模式	client.adjust_param('PDI3DFZ_RENDER_COLOR_SURFACE')
                    'pdi3dfz_color_threshold_up':'PDI3DFZ_COLOR_THRESHOLD_UP',			#增大3D血流阈值	client.adjust_param('PDI3DFZ_COLOR_THRESHOLD_UP')
                    'pdi3dfz_color_threshold_down':'PDI3DFZ_COLOR_THRESHOLD_DOWN',			#减小3D血流阈值	client.adjust_param('PDI3DFZ_COLOR_THRESHOLD_DOWN')
                    'pdi3dfz_transparency_up':'PDI3DFZ_TRANSPARENCY_UP',			#增大3D的透明度	client.adjust_param('PDI3DFZ_TRANSPARENCY_UP')
                    'pdi3dfz_transparency_down':'PDI3DFZ_TRANSPARENCY_DOWN',			#减小3D的透明度	client.adjust_param('PDI3DFZ_TRANSPARENCY_DOWN')
                    'pdi3dfz_brightness_up':'PDI3DFZ_BRIGHTNESS_UP',			#增大3D亮度	client.adjust_param('PDI3DFZ_BRIGHTNESS_UP')
                    'pdi3dfz_brightness_down':'PDI3DFZ_BRIGHTNESS_DOWN',			#减小3D亮度	client.adjust_param('PDI3DFZ_BRIGHTNESS_DOWN')
                    'pdi3dfz_smoothness_up':'PDI3DFZ_SMOOTHNESS_UP',			#增大3D平滑值	client.adjust_param('PDI3DFZ_SMOOTHNESS_UP')
                    'pdi3dfz_smoothness_down':'PDI3DFZ_SMOOTHNESS_DOWN',			#减小3D平滑值	client.adjust_param('PDI3DFZ_SMOOTHNESS_DOWN')
                    'pdi3dfz_color_chroma_down':'PDI3DFZ_COLOR_CHROMA_DOWN',			#减小3D彩色图谱值	client.adjust_param('PDI3DFZ_COLOR_CHROMA_DOWN')
                    'pdi3dfz_color_chroma_up':'PDI3DFZ_COLOR_CHROMA_UP',			#增大3D彩色图谱值	client.adjust_param('PDI3DFZ_COLOR_CHROMA_UP')
                    'pdi3dfz_bchroma_up':'PDI3DFZ_BCHROMA_UP',			#增大3D的B伪彩值	client.adjust_param('PDI3DFZ_BCHROMA_UP')
                    'pdi3dfz_bchroma_down':'PDI3DFZ_BCHROMA_DOWN',			#减小3D的B伪彩值	client.adjust_param('PDI3DFZ_BCHROMA_DOWN')
                    'pdi3dfz_render_color_grad_light':'PDI3DFZ_RENDER_COLOR_GRAD_LIGHT',			#开启3D血流梯度亮度渲染模式	client.adjust_param('PDI3DFZ_RENDER_COLOR_GRAD_LIGHT')
                    'pdi3dfz_render_glass_surface':'PDI3DFZ_RENDER_GLASS_SURFACE',			#开启3D的表面+表面成像渲染模式	client.adjust_param('PDI3DFZ_RENDER_GLASS_SURFACE')
                    'pdi3dfz_gray_color_ratio_down':'PDI3DFZ_GRAY_COLOR_RATIO_DOWN',			#减小3D的灰度/血流值	client.adjust_param('PDI3DFZ_GRAY_COLOR_RATIO_DOWN')
                    'pdi3dfz_gray_color_ratio_up':'PDI3DFZ_GRAY_COLOR_RATIO_UP',			#增大3D的灰度/血流值	client.adjust_param('PDI3DFZ_GRAY_COLOR_RATIO_UP')
                    'pdi3dfz_contrast_up':'PDI3DFZ_CONTRAST_UP',			#增大3D的对比度	client.adjust_param('PDI3DFZ_CONTRAST_UP')
                    'pdi3dfz_contrast_down':'PDI3DFZ_CONTRAST_DOWN',			#减小3D的对比度	client.adjust_param('PDI3DFZ_CONTRAST_DOWN')
                    'pdi3dfz_threshold_up':'PDI3DFZ_THRESHOLD_UP',			#增大3D阈值	client.adjust_param('PDI3DFZ_THRESHOLD_UP')
                    'pdi3dfz_threshold_down':'PDI3DFZ_THRESHOLD_DOWN',			#减小3D阈值	client.adjust_param('PDI3DFZ_THRESHOLD_DOWN')
                    'pdi3dfz_3dchroma_up':'PDI3DFZ_3DCHROMA_UP',			#增大3D的3D伪彩值	client.adjust_param('PDI3DFZ_3DCHROMA_UP')
                    'pdi3dfz_3dchroma_down':'PDI3DFZ_3DCHROMA_DOWN',			#减小3D的3D伪彩值	client.adjust_param('PDI3DFZ_3DCHROMA_DOWN')
                    'pdi3dfz_render_surface':'PDI3DFZ_RENDER_SURFACE',			#开启3D表面成像渲染模式	client.adjust_param('PDI3DFZ_RENDER_SURFACE')
                    'pdi3dfz_render_glass_surface_maxip':'PDI3DFZ_RENDER_GLASS_SURFACE_MAXIP',			#开启3D表面+最大密度渲染模式	client.adjust_param('PDI3DFZ_RENDER_GLASS_SURFACE_MAXIP')
                    'pdi3dfz_render_grad_light':'PDI3DFZ_RENDER_GRAD_LIGHT',			#开启3D梯度亮度渲染模式	client.adjust_param('PDI3DFZ_RENDER_GRAD_LIGHT')
                    'pdi3dfz_label_view':'PDI3DFZ_LABEL_VIEW',			#开启3D的视图页签	client.adjust_param('PDI3DFZ_LABEL_VIEW')
                    'pdi3dfz_rotate_45':'PDI3DFZ_ROTATE_45',			#45度自由旋转3D成像	client.adjust_param('PDI3DFZ_ROTATE_45')
                    'pdi3dfz_rotate_90':'PDI3DFZ_ROTATE_90',			#90度自由旋转3D成像	client.adjust_param('PDI3DFZ_ROTATE_90')
                    'pdi3dfz_rotate_360':'PDI3DFZ_ROTATE_360',			#360度自由旋转3D成像	client.adjust_param('PDI3DFZ_ROTATE_360')
                    'pdi3dfz_rotate_270':'PDI3DFZ_ROTATE_270',			#270度自由旋转3D成像	client.adjust_param('PDI3DFZ_ROTATE_270')
                    'pdi3dfz_rotate_180':'PDI3DFZ_ROTATE_180',			#180度自由旋转3D成像	client.adjust_param('PDI3DFZ_ROTATE_180')
                    'pdi3dfz_rotate_0':'PDI3DFZ_ROTATE_0',			#0度自由旋转3D成像	client.adjust_param('PDI3DFZ_ROTATE_0')
                    'pdi3dfz_direction_bottom':'PDI3DFZ_DIRECTION_BOTTOM',			#3D底部视图	client.adjust_param('PDI3DFZ_DIRECTION_BOTTOM')
                    'pdi3dfz_direction_top':'PDI3DFZ_DIRECTION_TOP',			#3D顶部视图	client.adjust_param('PDI3DFZ_DIRECTION_TOP')
                    'pdi3dfz_direction_left':'PDI3DFZ_DIRECTION_LEFT',			#3D左侧视图	client.adjust_param('PDI3DFZ_DIRECTION_LEFT')
                    'pdi3dfz_direction_right':'PDI3DFZ_DIRECTION_RIGHT',			#3D右侧视图	client.adjust_param('PDI3DFZ_DIRECTION_RIGHT')
                    'pdi3dfz_direction_fornt':'PDI3DFZ_DIRECTION_FORNT',			#3D前面视图	client.adjust_param('PDI3DFZ_DIRECTION_FORNT')
                    'pdi3dfz_direction_back':'PDI3DFZ_DIRECTION_BACK',			#3D后面视图	client.adjust_param('PDI3DFZ_DIRECTION_BACK')
                    'pdi3dfz_rotatex_up':'PDI3DFZ_ROTATEX_UP',			#增大3D的X旋转角度	client.adjust_param('PDI3DFZ_ROTATEX_UP')
                    'pdi3dfz_rotatex_down':'PDI3DFZ_ROTATEX_DOWN',			#减小3D的X旋转角度	client.adjust_param('PDI3DFZ_ROTATEX_DOWN')
                    'pdi3dfz_rotatey_up':'PDI3DFZ_ROTATEY_UP',			#增大3D的Y旋转角度	client.adjust_param('PDI3DFZ_ROTATEY_UP')
                    'pdi3dfz_rotatey_down':'PDI3DFZ_ROTATEY_DOWN',			#减小3D的Y旋转角度	client.adjust_param('PDI3DFZ_ROTATEY_DOWN')
                    'pdi3dfz_rotatez_up':'PDI3DFZ_ROTATEZ_UP',			#增大3D的Z旋转角度	client.adjust_param('PDI3DFZ_ROTATEZ_UP')
                    'pdi3dfz_rotatez_down':'PDI3DFZ_ROTATEZ_DOWN',			#减小3D的Z旋转角度	client.adjust_param('PDI3DFZ_ROTATEZ_DOWN')
                    'pdi3dfz_moveud_up':'PDI3DFZ_MOVEUD_UP',			#3D向上移动	client.adjust_param('PDI3DFZ_MOVEUD_UP')
                    'pdi3dfz_moveud_down':'PDI3DFZ_MOVEUD_DOWN',			#3D向下移动	client.adjust_param('PDI3DFZ_MOVEUD_DOWN')
                    'pdi3dfz_movelr_up':'PDI3DFZ_MOVELR_UP',			#3D向右移动	client.adjust_param('PDI3DFZ_MOVELR_UP')
                    'pdi3dfz_movelr_down':'PDI3DFZ_MOVELR_DOWN',			#3D向左移动	client.adjust_param('PDI3DFZ_MOVELR_DOWN')
                    'pdi3dfz_label_edit':'PDI3DFZ_LABEL_EDIT',			#开启3D编辑页签	client.adjust_param('PDI3DFZ_LABEL_EDIT')
                    'pdi3dfz_edit_rotate':'PDI3DFZ_EDIT_ROTATE',			#自由旋转3D成像	client.adjust_param('PDI3DFZ_EDIT_ROTATE')
                    'pdi3dfz_cut_method3':'PDI3DFZ_CUT_METHOD3',			#3D方框剪切区域内部分	client.adjust_param('PDI3DFZ_CUT_METHOD3')
                    'pdi3dfz_cut_method6':'PDI3DFZ_CUT_METHOD6',			#3D大橡皮擦剪切	client.adjust_param('PDI3DFZ_CUT_METHOD6')
                    'pdi3dfz_cut_method5':'PDI3DFZ_CUT_METHOD5',			#3D小橡皮擦剪切	client.adjust_param('PDI3DFZ_CUT_METHOD5')
                    'pdi3dfz_cut_method4':'PDI3DFZ_CUT_METHOD4',			#3D方框剪切区域外部分	client.adjust_param('PDI3DFZ_CUT_METHOD4')
                    'pdi3dfz_cut_method2':'PDI3DFZ_CUT_METHOD2',			#3D描迹剪切区域外部分	client.adjust_param('PDI3DFZ_CUT_METHOD2')
                    'pdi3dfz_cut_method1':'PDI3DFZ_CUT_METHOD1',			#3D描迹剪切区域内部分	client.adjust_param('PDI3DFZ_CUT_METHOD1')
                    'pdi3dfz_label_cplane':'PDI3DFZ_LABEL_CPLANE',			#开启3D截面页签	client.adjust_param('PDI3DFZ_LABEL_CPLANE')
                    'pdi3dfz_disp_ab':'PDI3DFZ_DISP_AB',			#显示3D的AB视图	client.adjust_param('PDI3DFZ_DISP_AB')
                    'pdi3dfz_cp_slice_b':'PDI3DFZ_CP_SLICE_B',			#选择3D的B视图进行层切	client.adjust_param('PDI3DFZ_CP_SLICE_B')
                    'pdi3dfz_cp_slice_a':'PDI3DFZ_CP_SLICE_A',			#选择3D的A视图进行层切	client.adjust_param('PDI3DFZ_CP_SLICE_A')
                    'pdi3dfz_disp_ac':'PDI3DFZ_DISP_AC',			#显示3D的AC视图	client.adjust_param('PDI3DFZ_DISP_AC')
                    'pdi3dfz_cp_slice_c':'PDI3DFZ_CP_SLICE_C',			#选择3D的C视图进行层切	client.adjust_param('PDI3DFZ_CP_SLICE_C')
                    'pdi3dfz_disp_bc':'PDI3DFZ_DISP_BC',			#显示3D的BC视图	client.adjust_param('PDI3DFZ_DISP_BC')
                    'pdi3dfz_disp_abc':'PDI3DFZ_DISP_ABC',			#显示3D的ABC视图	client.adjust_param('PDI3DFZ_DISP_ABC')
                    'pdi3dfz_cp_bchroma_up':'PDI3DFZ_CP_BCHROMA_UP',			#增大3D的B伪彩值	client.adjust_param('PDI3DFZ_CP_BCHROMA_UP')
                    'pdi3dfz_cp_bchroma_down':'PDI3DFZ_CP_BCHROMA_DOWN',			#减小3D的B伪彩值	client.adjust_param('PDI3DFZ_CP_BCHROMA_DOWN')
                    'pdi3dfz_label_mslice':'PDI3DFZ_LABEL_MSLICE',			#开启3D的断层切片页签	client.adjust_param('PDI3DFZ_LABEL_MSLICE')
                    'pdi3dfz_ms_slice_b':'PDI3DFZ_MS_SLICE_B',			#选择3D的B切片平面	client.adjust_param('PDI3DFZ_MS_SLICE_B')
                    'pdi3dfz_ms_slice_c':'PDI3DFZ_MS_SLICE_C',			#选择3D的C切片平面	client.adjust_param('PDI3DFZ_MS_SLICE_C')
                    'pdi3dfz_ms_slice_a':'PDI3DFZ_MS_SLICE_A',			#选择3D的A切片平面	client.adjust_param('PDI3DFZ_MS_SLICE_A')
                    'pdi3dfz_disp_12':'PDI3DFZ_DISP_12',			#设置3D显示模式为1*2	client.adjust_param('PDI3DFZ_DISP_12')
                    'pdi3dfz_disp_33':'PDI3DFZ_DISP_33',			#设置3D显示模式为3*3	client.adjust_param('PDI3DFZ_DISP_33')
                    'pdi3dfz_disp_44':'PDI3DFZ_DISP_44',			#设置3D显示模式为4*4	client.adjust_param('PDI3DFZ_DISP_44')
                    'pdi3dfz_disp_55':'PDI3DFZ_DISP_55',			#设置3D显示模式为5*5	client.adjust_param('PDI3DFZ_DISP_55')
                    'pdi3dfz_disp_34':'PDI3DFZ_DISP_34',			#设置3D显示模式为3*4	client.adjust_param('PDI3DFZ_DISP_34')
                    'pdi3dfz_disp_22':'PDI3DFZ_DISP_22',			#设置3D显示模式为2*2	client.adjust_param('PDI3DFZ_DISP_22')
                    'pdi3dfz_ms_bchroma_up':'PDI3DFZ_MS_BCHROMA_UP',			#增大3D断层切片的B伪彩值	client.adjust_param('PDI3DFZ_MS_BCHROMA_UP')
                    'pdi3dfz_ms_bchroma_down':'PDI3DFZ_MS_BCHROMA_DOWN',			#减小3D断层切片的B伪彩值	client.adjust_param('PDI3DFZ_MS_BCHROMA_DOWN')
                    'pdi3dfz_ms_adjustpos_up':'PDI3DFZ_MS_ADJUSTPOS_UP',			#微增大3D所选切片的位置	client.adjust_param('PDI3DFZ_MS_ADJUSTPOS_UP')
                    'pdi3dfz_ms_adjustpos_down':'PDI3DFZ_MS_ADJUSTPOS_DOWN',			#微减小3D所选切片的位置	client.adjust_param('PDI3DFZ_MS_ADJUSTPOS_DOWN')
                    'pdi3dfz_ms_distance_up':'PDI3DFZ_MS_DISTANCE_UP',			#增大3D切片间距	client.adjust_param('PDI3DFZ_MS_DISTANCE_UP')
                    'pdi3dfz_ms_distance_down':'PDI3DFZ_MS_DISTANCE_DOWN',			#减小3D切片间距	client.adjust_param('PDI3DFZ_MS_DISTANCE_DOWN')
                    'pdi3dfz_ms_slicenum_up':'PDI3DFZ_MS_SLICENUM_UP',			#增多3D切片数量	client.adjust_param('PDI3DFZ_MS_SLICENUM_UP')
                    'pdi3dfz_ms_slicenum_down':'PDI3DFZ_MS_SLICENUM_DOWN',			#减少3D切片数量	client.adjust_param('PDI3DFZ_MS_SLICENUM_DOWN')
                    'pdi3dfz_ms_display_up':'PDI3DFZ_MS_DISPLAY_UP',			#向右平移3D切片区域所有切片	client.adjust_param('PDI3DFZ_MS_DISPLAY_UP')
                    'pdi3dfz_ms_display_down':'PDI3DFZ_MS_DISPLAY_DOWN',			#向左平移3D切片区域所有切片	client.adjust_param('PDI3DFZ_MS_DISPLAY_DOWN')
                    'pdi3dfz_volpre':'PDI3DFZ_VOLPRE',			#返回3D预激活模式	client.adjust_param('PDI3DFZ_VOLPRE')
                    # FH-3D4D
                    'fh3dfz_edit_roi':'FH3DFZ_EDIT_ROI',			#编辑ROI锁定3D视图	client.adjust_param('FH3DFZ_EDIT_ROI')
                    'fh3dfz_rotate':'FH3DFZ_ROTATE',			#自由旋转3D成像	client.adjust_param('FH3DFZ_ROTATE')
                    'fh3dfz_orient_0':'FH3DFZ_ORIENT_0',			#0度旋转3D	client.adjust_param('FH3DFZ_ORIENT_0')
                    'fh3dfz_orient_90':'FH3DFZ_ORIENT_90',			#90度旋转3D	client.adjust_param('FH3DFZ_ORIENT_90')
                    'fh3dfz_reset':'FH3DFZ_RESET',			#复位3D	client.adjust_param('FH3DFZ_RESET')
                    'fh3dfz_orient_270':'FH3DFZ_ORIENT_270',			#270度旋转3D	client.adjust_param('FH3DFZ_ORIENT_270')
                    'fh3dfz_orient_180':'FH3DFZ_ORIENT_180',			#180度旋转3D	client.adjust_param('FH3DFZ_ORIENT_180')
                    'fh3dfz_disp_full':'FH3DFZ_DISP_FULL',			#3D单幅显示	client.adjust_param('FH3DFZ_DISP_FULL')
                    'fh3dfz_slice_3d':'FH3DFZ_SLICE_3D',			#选择3D图像	client.adjust_param('FH3DFZ_SLICE_3D')
                    'fh3dfz_disp_dual':'FH3DFZ_DISP_DUAL',			#3D双幅显示	client.adjust_param('FH3DFZ_DISP_DUAL')
                    'fh3dfz_slice_a':'FH3DFZ_SLICE_A',			#选择3D的A视图	client.adjust_param('FH3DFZ_SLICE_A')
                    'fh3dfz_disp_quad':'FH3DFZ_DISP_QUAD',			#3D四幅显示	client.adjust_param('FH3DFZ_DISP_QUAD')
                    'fh3dfz_slice_b':'FH3DFZ_SLICE_B',			#选择3D的B视图	client.adjust_param('FH3DFZ_SLICE_B')
                    'fh3dfz_slice_c':'FH3DFZ_SLICE_C',			#选择3D的C视图	client.adjust_param('FH3DFZ_SLICE_C')
                    'fh3dfz_render_surface':'FH3DFZ_RENDER_SURFACE',			#开启3D表面成像渲染模式	client.adjust_param('FH3DFZ_RENDER_SURFACE')
                    'fh3dfz_threshold_down':'FH3DFZ_THRESHOLD_DOWN',			#减小3D阈值	client.adjust_param('FH3DFZ_THRESHOLD_DOWN')
                    'fh3dfz_threshold_up':'FH3DFZ_THRESHOLD_UP',			#增大3D阈值	client.adjust_param('FH3DFZ_THRESHOLD_UP')
                    'fh3dfz_contrast_down':'FH3DFZ_CONTRAST_DOWN',			#减小3D的对比度	client.adjust_param('FH3DFZ_CONTRAST_DOWN')
                    'fh3dfz_contrast_up':'FH3DFZ_CONTRAST_UP',			#增大3D的对比度	client.adjust_param('FH3DFZ_CONTRAST_UP')
                    'fh3dfz_transparency_down':'FH3DFZ_TRANSPARENCY_DOWN',			#减小3D的透明度	client.adjust_param('FH3DFZ_TRANSPARENCY_DOWN')
                    'fh3dfz_transparency_up':'FH3DFZ_TRANSPARENCY_UP',			#增大3D的透明度	client.adjust_param('FH3DFZ_TRANSPARENCY_UP')
                    'fh3dfz_brightness_down':'FH3DFZ_BRIGHTNESS_DOWN',			#减小3D亮度	client.adjust_param('FH3DFZ_BRIGHTNESS_DOWN')
                    'fh3dfz_brightness_up':'FH3DFZ_BRIGHTNESS_UP',			#增大3D亮度	client.adjust_param('FH3DFZ_BRIGHTNESS_UP')
                    'fh3dfz_smoothness_down':'FH3DFZ_SMOOTHNESS_DOWN',			#减小3D平滑值	client.adjust_param('FH3DFZ_SMOOTHNESS_DOWN')
                    'fh3dfz_smoothness_up':'FH3DFZ_SMOOTHNESS_UP',			#增大3D平滑值	client.adjust_param('FH3DFZ_SMOOTHNESS_UP')
                    'fh3dfz_3dchroma_down':'FH3DFZ_3DCHROMA_DOWN',			#减小3D的3D伪彩值	client.adjust_param('FH3DFZ_3DCHROMA_DOWN')
                    'fh3dfz_3dchroma_up':'FH3DFZ_3DCHROMA_UP',			#增大3D的3D伪彩值	client.adjust_param('FH3DFZ_3DCHROMA_UP')
                    'fh3dfz_bchroma_down':'FH3DFZ_BCHROMA_DOWN',			#减小3D的B伪彩值	client.adjust_param('FH3DFZ_BCHROMA_DOWN')
                    'fh3dfz_bchroma_up':'FH3DFZ_BCHROMA_UP',			#增大3D的B伪彩值	client.adjust_param('FH3DFZ_BCHROMA_UP')
                    'fh3dfz_label_view':'FH3DFZ_LABEL_VIEW',			#开启3D的视图页签	client.adjust_param('FH3DFZ_LABEL_VIEW')
                    'fh3dfz_sector':'FH3DFZ_SECTOR',			#开启扇扫功能	client.adjust_param('FH3DFZ_SECTOR')
                    'fh3dfz_label_3d4d':'FH3DFZ_LABEL_3D4D',			#开启3D4D页签	client.adjust_param('FH3DFZ_LABEL_3D4D')
                    'fh3dfz_sector_z_angle_down':'FH3DFZ_SECTOR_Z_ANGLE_DOWN',			#减小3D的Z角度	client.adjust_param('FH3DFZ_SECTOR_Z_ANGLE_DOWN')
                    'fh3dfz_sector_z_angle_up':'FH3DFZ_SECTOR_Z_ANGLE_UP',			#增大3D的Z角度	client.adjust_param('FH3DFZ_SECTOR_Z_ANGLE_UP')
                    'fh3dfz_linear':'FH3DFZ_LINEAR',			#开启线扫功能	client.adjust_param('FH3DFZ_LINEAR')
                    'fh3dfz_linear_z_scale_dowm':'FH3DFZ_LINEAR_Z_SCALE_DOWM',			#减小3D的Z缩放	client.adjust_param('FH3DFZ_LINEAR_Z_SCALE_DOWM')
                    'fh3dfz_linear_z_scale_up':'FH3DFZ_LINEAR_Z_SCALE_UP',			#增大3D的Z缩放	client.adjust_param('FH3DFZ_LINEAR_Z_SCALE_UP')
                    'fh3dfz_render_grad_light':'FH3DFZ_RENDER_GRAD_LIGHT',			#开启3D梯度亮度渲染模式	client.adjust_param('FH3DFZ_RENDER_GRAD_LIGHT')
                    'fh3dfz_render_skeleton':'FH3DFZ_RENDER_SKELETON',			#开启3D骨骼成像渲染模式	client.adjust_param('FH3DFZ_RENDER_SKELETON')
                    'fh3dfz_skeleton_depth':'FH3DFZ_SKELETON_DEPTH',			#开启3D骨骼深度成像	client.adjust_param('FH3DFZ_SKELETON_DEPTH')
                    'fh3dfz_skeleton':'FH3DFZ_SKELETON',			#开启3D骨骼成像	client.adjust_param('FH3DFZ_SKELETON')
                    'fh3dfz_render_transp_min':'FH3DFZ_RENDER_TRANSP_MIN',			#开启3D最小回声成像渲染模式	client.adjust_param('FH3DFZ_RENDER_TRANSP_MIN')
                    'fh3dfz_render_xray':'FH3DFZ_RENDER_XRAY',			#开启3D的X-线成像渲染模式	client.adjust_param('FH3DFZ_RENDER_XRAY')
                    'fh3dfz_render_sdepth':'FH3DFZ_RENDER_SDEPTH',			#开启3D深度成像渲染模式	client.adjust_param('FH3DFZ_RENDER_SDEPTH')
                    'fh3dfz_render_slive':'FH3DFZ_RENDER_SLIVE',			#开启3D的S-Live渲染模式	client.adjust_param('FH3DFZ_RENDER_SLIVE')
                    'fh3dfz_light_pos_down':'FH3DFZ_LIGHT_POS_DOWN',			#减小3D的灯光位置	client.adjust_param('FH3DFZ_LIGHT_POS_DOWN')
                    'fh3dfz_light_pos_up':'FH3DFZ_LIGHT_POS_UP',			#增大3D的灯光位置	client.adjust_param('FH3DFZ_LIGHT_POS_UP')
                    'fh3dfz_slive_silhouette':'FH3DFZ_SLIVE_SILHOUETTE',			#开启3D的S-Live Silhouette结构	client.adjust_param('FH3DFZ_SLIVE_SILHOUETTE')
                    'fh3dfz_edit_light':'FH3DFZ_EDIT_LIGHT',			#开启3D调节灯光功能	client.adjust_param('FH3DFZ_EDIT_LIGHT')
                    'fh3dfz_slive':'FH3DFZ_SLIVE',			#开启3D的S-Live结构	client.adjust_param('FH3DFZ_SLIVE')
                    'fh3dfz_rotate_45':'FH3DFZ_ROTATE_45',			#45度自由旋转3D成像	client.adjust_param('FH3DFZ_ROTATE_45')
                    'fh3dfz_rotate_90':'FH3DFZ_ROTATE_90',			#90度自由旋转3D成像	client.adjust_param('FH3DFZ_ROTATE_90')
                    'fh3dfz_rotate_360':'FH3DFZ_ROTATE_360',			#360度自由旋转3D成像	client.adjust_param('FH3DFZ_ROTATE_360')
                    'fh3dfz_rotate_270':'FH3DFZ_ROTATE_270',			#270度自由旋转3D成像	client.adjust_param('FH3DFZ_ROTATE_270')
                    'fh3dfz_rotate_180':'FH3DFZ_ROTATE_180',			#180度自由旋转3D成像	client.adjust_param('FH3DFZ_ROTATE_180')
                    'fh3dfz_rotate_0':'FH3DFZ_ROTATE_0',			#0度自由旋转3D成像	client.adjust_param('FH3DFZ_ROTATE_0')
                    'fh3dfz_direction_left':'FH3DFZ_DIRECTION_LEFT',			#3D左侧视图	client.adjust_param('FH3DFZ_DIRECTION_LEFT')
                    'fh3dfz_direction_fornt':'FH3DFZ_DIRECTION_FORNT',			#3D前面视图	client.adjust_param('FH3DFZ_DIRECTION_FORNT')
                    'fh3dfz_direction_back':'FH3DFZ_DIRECTION_BACK',			#3D后面视图	client.adjust_param('FH3DFZ_DIRECTION_BACK')
                    'fh3dfz_direction_right':'FH3DFZ_DIRECTION_RIGHT',			#3D右侧视图	client.adjust_param('FH3DFZ_DIRECTION_RIGHT')
                    'fh3dfz_direction_bottom':'FH3DFZ_DIRECTION_BOTTOM',			#3D底部视图	client.adjust_param('FH3DFZ_DIRECTION_BOTTOM')
                    'fh3dfz_direction_top':'FH3DFZ_DIRECTION_TOP',			#3D顶部视图	client.adjust_param('FH3DFZ_DIRECTION_TOP')
                    'fh3dfz_rotatex_down':'FH3DFZ_ROTATEX_DOWN',			#减小3D的X旋转角度	client.adjust_param('FH3DFZ_ROTATEX_DOWN')
                    'fh3dfz_rotatex_up':'FH3DFZ_ROTATEX_UP',			#增大3D的X旋转角度	client.adjust_param('FH3DFZ_ROTATEX_UP')
                    'fh3dfz_rotatey_down':'FH3DFZ_ROTATEY_DOWN',			#减小3D的Y旋转角度	client.adjust_param('FH3DFZ_ROTATEY_DOWN')
                    'fh3dfz_rotatey_up':'FH3DFZ_ROTATEY_UP',			#增大3D的Y旋转角度	client.adjust_param('FH3DFZ_ROTATEY_UP')
                    'fh3dfz_rotatez_down':'FH3DFZ_ROTATEZ_DOWN',			#减小3D的Z旋转角度	client.adjust_param('FH3DFZ_ROTATEZ_DOWN')
                    'fh3dfz_rotatez_up':'FH3DFZ_ROTATEZ_UP',			#增大3D的Z旋转角度	client.adjust_param('FH3DFZ_ROTATEZ_UP')
                    'fh3dfz_moveud_down':'FH3DFZ_MOVEUD_DOWN',			#3D向下移动	client.adjust_param('FH3DFZ_MOVEUD_DOWN')
                    'fh3dfz_moveud_up':'FH3DFZ_MOVEUD_UP',			#3D向上移动	client.adjust_param('FH3DFZ_MOVEUD_UP')
                    'fh3dfz_movelr_down':'FH3DFZ_MOVELR_DOWN',			#3D向左移动	client.adjust_param('FH3DFZ_MOVELR_DOWN')
                    'fh3dfz_movelr_up':'FH3DFZ_MOVELR_UP',			#3D向右移动	client.adjust_param('FH3DFZ_MOVELR_UP')
                    'fh3dfz_label_edit':'FH3DFZ_LABEL_EDIT',			#开启3D编辑页签	client.adjust_param('FH3DFZ_LABEL_EDIT')
                    'fh3dfz_edit_rotate':'FH3DFZ_EDIT_ROTATE',			#自由旋转3D成像	client.adjust_param('FH3DFZ_EDIT_ROTATE')
                    'fh3dfz_cut_method3':'FH3DFZ_CUT_METHOD3',			#3D方框剪切区域内部分	client.adjust_param('FH3DFZ_CUT_METHOD3')
                    'fh3dfz_cut_method6':'FH3DFZ_CUT_METHOD6',			#3D大橡皮擦剪切	client.adjust_param('FH3DFZ_CUT_METHOD6')
                    'fh3dfz_cut_method5':'FH3DFZ_CUT_METHOD5',			#3D小橡皮擦剪切	client.adjust_param('FH3DFZ_CUT_METHOD5')
                    'fh3dfz_cut_method4':'FH3DFZ_CUT_METHOD4',			#3D方框剪切区域外部分	client.adjust_param('FH3DFZ_CUT_METHOD4')
                    'fh3dfz_cut_method2':'FH3DFZ_CUT_METHOD2',			#3D描迹剪切区域外部分	client.adjust_param('FH3DFZ_CUT_METHOD2')
                    'fh3dfz_cut_method1':'FH3DFZ_CUT_METHOD1',			#3D描迹剪切区域内部分	client.adjust_param('FH3DFZ_CUT_METHOD1')
                    'fh3dfz_label_cplane':'FH3DFZ_LABEL_CPLANE',			#开启3D的截面页签	client.adjust_param('FH3DFZ_LABEL_CPLANE')
                    'fh3dfz_disp_ab':'FH3DFZ_DISP_AB',			#显示3D的AB视图	client.adjust_param('FH3DFZ_DISP_AB')
                    'fh3dfz_cp_slice_b':'FH3DFZ_CP_SLICE_B',			#选择3D的B视图进行层切	client.adjust_param('FH3DFZ_CP_SLICE_B')
                    'fh3dfz_cp_slice_a':'FH3DFZ_CP_SLICE_A',			#选择3D的A视图进行层切	client.adjust_param('FH3DFZ_CP_SLICE_A')
                    'fh3dfz_disp_ac':'FH3DFZ_DISP_AC',			#显示3D的AC视图	client.adjust_param('FH3DFZ_DISP_AC')
                    'fh3dfz_cp_slice_c':'FH3DFZ_CP_SLICE_C',			#选择3D的C视图进行层切	client.adjust_param('FH3DFZ_CP_SLICE_C')
                    'fh3dfz_disp_bc':'FH3DFZ_DISP_BC',			#显示3D的BC视图	client.adjust_param('FH3DFZ_DISP_BC')
                    'fh3dfz_disp_abc':'FH3DFZ_DISP_ABC',			#显示3D的ABC视图	client.adjust_param('FH3DFZ_DISP_ABC')
                    'fh3dfz_cp_bchroma_down':'FH3DFZ_CP_BCHROMA_DOWN',			#减小3D的B伪彩值	client.adjust_param('FH3DFZ_CP_BCHROMA_DOWN')
                    'fh3dfz_cp_bchroma_up':'FH3DFZ_CP_BCHROMA_UP',			#增大3D的B伪彩值	client.adjust_param('FH3DFZ_CP_BCHROMA_UP')
                    'fh3dfz_label_mslice':'FH3DFZ_LABEL_MSLICE',			#开启3D的断层切片页签	client.adjust_param('FH3DFZ_LABEL_MSLICE')
                    'fh3dfz_ms_slice_b':'FH3DFZ_MS_SLICE_B',			#选择3D的B切片平面	client.adjust_param('FH3DFZ_MS_SLICE_B')
                    'fh3dfz_ms_slice_c':'FH3DFZ_MS_SLICE_C',			#选择3D的C切片平面	client.adjust_param('FH3DFZ_MS_SLICE_C')
                    'fh3dfz_ms_slice_a':'FH3DFZ_MS_SLICE_A',			#选择3D的A切片平面	client.adjust_param('FH3DFZ_MS_SLICE_A')
                    'fh3dfz_disp_12':'FH3DFZ_DISP_12',			#设置3D显示模式为1*2	client.adjust_param('FH3DFZ_DISP_12')
                    'fh3dfz_disp_33':'FH3DFZ_DISP_33',			#设置3D显示模式为3*3	client.adjust_param('FH3DFZ_DISP_33')
                    'fh3dfz_disp_44':'FH3DFZ_DISP_44',			#设置3D显示模式为4*4	client.adjust_param('FH3DFZ_DISP_44')
                    'fh3dfz_disp_55':'FH3DFZ_DISP_55',			#设置3D显示模式为5*5	client.adjust_param('FH3DFZ_DISP_55')
                    'fh3dfz_disp_34':'FH3DFZ_DISP_34',			#设置3D显示模式为3*4	client.adjust_param('FH3DFZ_DISP_34')
                    'fh3dfz_disp_22':'FH3DFZ_DISP_22',			#设置3D显示模式为2*2	client.adjust_param('FH3DFZ_DISP_22')
                    'fh3dfz_ms_bchroma_down':'FH3DFZ_MS_BCHROMA_DOWN',			#减小3D断层切片的B伪彩值	client.adjust_param('FH3DFZ_MS_BCHROMA_DOWN')
                    'fh3dfz_ms_bchroma_up':'FH3DFZ_MS_BCHROMA_UP',			#增大3D断层切片的B伪彩值	client.adjust_param('FH3DFZ_MS_BCHROMA_UP')
                    'fh3dfz_ms_adjustpos_down':'FH3DFZ_MS_ADJUSTPOS_DOWN',			#微减小3D所选切片的位置	client.adjust_param('FH3DFZ_MS_ADJUSTPOS_DOWN')
                    'fh3dfz_ms_adjustpos_up':'FH3DFZ_MS_ADJUSTPOS_UP',			#微增大3D所选切片的位置	client.adjust_param('FH3DFZ_MS_ADJUSTPOS_UP')
                    'fh3dfz_ms_distance_down':'FH3DFZ_MS_DISTANCE_DOWN',			#减小3D切片间距	client.adjust_param('FH3DFZ_MS_DISTANCE_DOWN')
                    'fh3dfz_ms_distance_up':'FH3DFZ_MS_DISTANCE_UP',			#增大3D切片间距	client.adjust_param('FH3DFZ_MS_DISTANCE_UP')
                    'fh3dfz_ms_slicenum_down':'FH3DFZ_MS_SLICENUM_DOWN',			#减少3D切片数量	client.adjust_param('FH3DFZ_MS_SLICENUM_DOWN')
                    'fh3dfz_ms_slicenum_up':'FH3DFZ_MS_SLICENUM_UP',			#增多3D切片数量	client.adjust_param('FH3DFZ_MS_SLICENUM_UP')
                    'fh3dfz_ms_display_down':'FH3DFZ_MS_DISPLAY_DOWN',			#向左平移3D切片区域所有切片	client.adjust_param('FH3DFZ_MS_DISPLAY_DOWN')
                    'fh3dfz_ms_display_up':'FH3DFZ_MS_DISPLAY_UP',			#向右平移3D切片区域所有切片	client.adjust_param('FH3DFZ_MS_DISPLAY_UP')
                    'fh3dfz_label_avc':'FH3DFZ_LABEL_AVC',			#开启3D卵泡自动测量页签	client.adjust_param('FH3DFZ_LABEL_AVC')
                    'fh3dfz_leftovary':'FH3DFZ_LEFTOVARY',			#开启3D左侧卵巢	client.adjust_param('FH3DFZ_LEFTOVARY')
                    'fh3dfz_rightovary':'FH3DFZ_RIGHTOVARY',			#开启3D右侧卵巢	client.adjust_param('FH3DFZ_RIGHTOVARY')
                    'fh3dfz_avc_slice_b':'FH3DFZ_AVC_SLICE_B',			#显示卵泡3D的B视图	client.adjust_param('FH3DFZ_AVC_SLICE_B')
                    'fh3dfz_avc_slice_3d':'FH3DFZ_AVC_SLICE_3D',			#显示卵泡3D的3D图像	client.adjust_param('FH3DFZ_AVC_SLICE_3D')
                    'fh3dfz_avc_slice_c':'FH3DFZ_AVC_SLICE_C',			#显示卵泡3D的C视图	client.adjust_param('FH3DFZ_AVC_SLICE_C')
                    'fh3dfz_avc_slice_a':'FH3DFZ_AVC_SLICE_A',			#显示卵泡3D的A视图	client.adjust_param('FH3DFZ_AVC_SLICE_A')
                    'fh3dfz_ms_thlow_down':'FH3DFZ_MS_THLOW_DOWN',			#减小3D低回声阈值	client.adjust_param('FH3DFZ_MS_THLOW_DOWN')
                    'fh3dfz_ms_thlow_up':'FH3DFZ_MS_THLOW_UP',			#增大3D低回声阈值	client.adjust_param('FH3DFZ_MS_THLOW_UP')
                    'fh3dfz_ms_brightness_down':'FH3DFZ_MS_BRIGHTNESS_DOWN',			#减小3D卵泡亮度	client.adjust_param('FH3DFZ_MS_BRIGHTNESS_DOWN')
                    'fh3dfz_ms_brightness_up':'FH3DFZ_MS_BRIGHTNESS_UP',			#增大3D卵泡亮度	client.adjust_param('FH3DFZ_MS_BRIGHTNESS_UP')
                    # CONTRAST-3D
                    'contrast_4dpa_label_contrast3d':'CONTRAST_4DPA_LABEL_CONTRAST3D',			#开启造影3D模式	client.adjust_param('CONTRAST_4DPA_LABEL_CONTRAST3D')
                    'contrast_3dpa_user_mode1':'CONTRAST_3DPA_USER_MODE1',			#开启3D第一个用户模式	client.adjust_param('CONTRAST_3DPA_USER_MODE1')
                    'contrast_3dpa_user_mode2':'CONTRAST_3DPA_USER_MODE2',			#开启3D第二个用户模式	client.adjust_param('CONTRAST_3DPA_USER_MODE2')
                    'contrast_3dpa_user_mode3':'CONTRAST_3DPA_USER_MODE3',			#开启3D第三个用户模式	client.adjust_param('CONTRAST_3DPA_USER_MODE3')
                    'contrast_3dpa_disp_full':'CONTRAST_3DPA_DISP_FULL',			#3D预激活单幅显示	client.adjust_param('CONTRAST_3DPA_DISP_FULL')
                    'contrast_3dpa_disp_dual':'CONTRAST_3DPA_DISP_DUAL',			#3D预激活双幅显示	client.adjust_param('CONTRAST_3DPA_DISP_DUAL')
                    'contrast_3dpa_disp_quad':'CONTRAST_3DPA_DISP_QUAD',			#3D预激活四幅显示	client.adjust_param('CONTRAST_3DPA_DISP_QUAD')
                    'contrast_3dpa_focus_down':'CONTRAST_3DPA_FOCUS_DOWN',			#减小3D焦点位置	client.adjust_param('CONTRAST_3DPA_FOCUS_DOWN')
                    'contrast_3dpa_focus_up':'CONTRAST_3DPA_FOCUS_UP',			#增大3D焦点位置	client.adjust_param('CONTRAST_3DPA_FOCUS_UP')
                    'contrast_3dpa_image_quality_down':'CONTRAST_3DPA_IMAGE_QUALITY_DOWN',			#减小3D图像质量	client.adjust_param('CONTRAST_3DPA_IMAGE_QUALITY_DOWN')
                    'contrast_3dpa_image_quality_up':'CONTRAST_3DPA_IMAGE_QUALITY_UP',			#增大3D图像质量	client.adjust_param('CONTRAST_3DPA_IMAGE_QUALITY_UP')
                    'contrast_3dpa_sweep_angle_down':'CONTRAST_3DPA_SWEEP_ANGLE_DOWN',			#减小3D摆动角度	client.adjust_param('CONTRAST_3DPA_SWEEP_ANGLE_DOWN')
                    'contrast_3dpa_sweep_angle_up':'CONTRAST_3DPA_SWEEP_ANGLE_UP',			#增大3D摆动角度	client.adjust_param('CONTRAST_3DPA_SWEEP_ANGLE_UP')
                    'contrast_3dpa_start':'CONTRAST_3DPA_START',			#开启3D实时模式	client.adjust_param('CONTRAST_3DPA_START')
                    'contrast_3dfz_label_3d4d':'CONTRAST_3DFZ_LABEL_3D4D',			#进入3D/4D页签	client.adjust_param('CONTRAST_3DFZ_LABEL_3D4D')
                    'contrast_3dfz_render_surface':'CONTRAST_3DFZ_RENDER_SURFACE',			#开启3D表面成像渲染模式	client.adjust_param('CONTRAST_3DFZ_RENDER_SURFACE')
                    'contrast_3dfz_edit_roi':'CONTRAST_3DFZ_EDIT_ROI',			#编辑ROI锁定3D视图	client.adjust_param('CONTRAST_3DFZ_EDIT_ROI')
                    'contrast_3dfz_inversion':'CONTRAST_3DFZ_INVERSION',			#反转3D成像	client.adjust_param('CONTRAST_3DFZ_INVERSION')
                    'contrast_3dfz_rotate':'CONTRAST_3DFZ_ROTATE',			#自由旋转3D成像	client.adjust_param('CONTRAST_3DFZ_ROTATE')
                    'contrast_3dfz_autoface':'CONTRAST_3DFZ_AUTOFACE',			#一键显脸	client.adjust_param('CONTRAST_3DFZ_AUTOFACE')
                    'contrast_3dfz_disp_full':'CONTRAST_3DFZ_DISP_FULL',			#3D实时单幅显示	client.adjust_param('CONTRAST_3DFZ_DISP_FULL')
                    'contrast_3dfz_disp_dual':'CONTRAST_3DFZ_DISP_DUAL',			#3D实时双幅显示	client.adjust_param('CONTRAST_3DFZ_DISP_DUAL')
                    'contrast_3dfz_disp_quad':'CONTRAST_3DFZ_DISP_QUAD',			#3D实时四幅显示	client.adjust_param('CONTRAST_3DFZ_DISP_QUAD')
                    'contrast_3dfz_orient_90':'CONTRAST_3DFZ_ORIENT_90',			#90度旋转3D	client.adjust_param('CONTRAST_3DFZ_ORIENT_90')
                    'contrast_3dfz_orient_270':'CONTRAST_3DFZ_ORIENT_270',			#270度旋转3D	client.adjust_param('CONTRAST_3DFZ_ORIENT_270')
                    'contrast_3dfz_reset':'CONTRAST_3DFZ_RESET',			#复位3D	client.adjust_param('CONTRAST_3DFZ_RESET')
                    'contrast_3dfz_orient_180':'CONTRAST_3DFZ_ORIENT_180',			#180度旋转3D	client.adjust_param('CONTRAST_3DFZ_ORIENT_180')
                    'contrast_3dfz_orient_0':'CONTRAST_3DFZ_ORIENT_0',			#0度旋转3D	client.adjust_param('CONTRAST_3DFZ_ORIENT_0')
                    'contrast_3dfz_slice_b':'CONTRAST_3DFZ_SLICE_B',			#选择3D的B视图	client.adjust_param('CONTRAST_3DFZ_SLICE_B')
                    'contrast_3dfz_slice_3d':'CONTRAST_3DFZ_SLICE_3D',			#选择3D图像	client.adjust_param('CONTRAST_3DFZ_SLICE_3D')
                    'contrast_3dfz_slice_c':'CONTRAST_3DFZ_SLICE_C',			#选择3D的C视图	client.adjust_param('CONTRAST_3DFZ_SLICE_C')
                    'contrast_3dfz_slice_a':'CONTRAST_3DFZ_SLICE_A',			#选择3D的A视图	client.adjust_param('CONTRAST_3DFZ_SLICE_A')
                    'contrast_3dfz_threshold_down':'CONTRAST_3DFZ_THRESHOLD_DOWN',			#减小3D阈值	client.adjust_param('CONTRAST_3DFZ_THRESHOLD_DOWN')
                    'contrast_3dfz_threshold_up':'CONTRAST_3DFZ_THRESHOLD_UP',			#增大3D阈值	client.adjust_param('CONTRAST_3DFZ_THRESHOLD_UP')
                    'contrast_3dfz_contrast_down':'CONTRAST_3DFZ_CONTRAST_DOWN',			#减小3D的对比度	client.adjust_param('CONTRAST_3DFZ_CONTRAST_DOWN')
                    'contrast_3dfz_contrast_up':'CONTRAST_3DFZ_CONTRAST_UP',			#增大3D的对比度	client.adjust_param('CONTRAST_3DFZ_CONTRAST_UP')
                    'contrast_3dfz_transparency_down':'CONTRAST_3DFZ_TRANSPARENCY_DOWN',			#减小3D的透明度	client.adjust_param('CONTRAST_3DFZ_TRANSPARENCY_DOWN')
                    'contrast_3dfz_transparency_up':'CONTRAST_3DFZ_TRANSPARENCY_UP',			#增大3D的透明度	client.adjust_param('CONTRAST_3DFZ_TRANSPARENCY_UP')
                    'contrast_3dfz_brightness_down':'CONTRAST_3DFZ_BRIGHTNESS_DOWN',			#减小3D亮度	client.adjust_param('CONTRAST_3DFZ_BRIGHTNESS_DOWN')
                    'contrast_3dfz_brightness_up':'CONTRAST_3DFZ_BRIGHTNESS_UP',			#增大3D亮度	client.adjust_param('CONTRAST_3DFZ_BRIGHTNESS_UP')
                    'contrast_3dfz_smoothness_down':'CONTRAST_3DFZ_SMOOTHNESS_DOWN',			#减小3D平滑值	client.adjust_param('CONTRAST_3DFZ_SMOOTHNESS_DOWN')
                    'contrast_3dfz_smoothness_up':'CONTRAST_3DFZ_SMOOTHNESS_UP',			#增大3D平滑值	client.adjust_param('CONTRAST_3DFZ_SMOOTHNESS_UP')
                    'contrast_3dfz_2duscan_down':'CONTRAST_3DFZ_2DUSCAN_DOWN',			#减小3D的2D微米成像值	client.adjust_param('CONTRAST_3DFZ_2DUSCAN_DOWN')
                    'contrast_3dfz_2duscan_up':'CONTRAST_3DFZ_2DUSCAN_UP',			#增大3D的2D微米成像值	client.adjust_param('CONTRAST_3DFZ_2DUSCAN_UP')
                    'contrast_3dfz_3duscan_down':'CONTRAST_3DFZ_3DUSCAN_DOWN',			#减小3D的3D微米成像值	client.adjust_param('CONTRAST_3DFZ_3DUSCAN_DOWN')
                    'contrast_3dfz_3duscan_up':'CONTRAST_3DFZ_3DUSCAN_UP',			#增大3D的3D微米成像值	client.adjust_param('CONTRAST_3DFZ_3DUSCAN_UP')
                    'contrast_3dfz_3dchroma_down':'CONTRAST_3DFZ_3DCHROMA_DOWN',			#减小3D的3D伪彩值	client.adjust_param('CONTRAST_3DFZ_3DCHROMA_DOWN')
                    'contrast_3dfz_3dchroma_up':'CONTRAST_3DFZ_3DCHROMA_UP',			#增大3D的3D伪彩值	client.adjust_param('CONTRAST_3DFZ_3DCHROMA_UP')
                    'contrast_3dfz_bchroma_down':'CONTRAST_3DFZ_BCHROMA_DOWN',			#减小3D的B伪彩值	client.adjust_param('CONTRAST_3DFZ_BCHROMA_DOWN')
                    'contrast_3dfz_bchroma_up':'CONTRAST_3DFZ_BCHROMA_UP',			#增大3D的B伪彩值	client.adjust_param('CONTRAST_3DFZ_BCHROMA_UP')
                    'contrast_3dfz_label_cplane':'CONTRAST_3DFZ_LABEL_CPLANE',			#开启3D截面页签	client.adjust_param('CONTRAST_3DFZ_LABEL_CPLANE')
                    'contrast_3dfz_cp_2duscan_down':'CONTRAST_3DFZ_CP_2DUSCAN_DOWN',			#减小3D截面2D微米成像	client.adjust_param('CONTRAST_3DFZ_CP_2DUSCAN_DOWN')
                    'contrast_3dfz_cp_2duscan_up':'CONTRAST_3DFZ_CP_2DUSCAN_UP',			#增大3D截面2D微米成像	client.adjust_param('CONTRAST_3DFZ_CP_2DUSCAN_UP')
                    'contrast_3dfz_render_grad_light':'CONTRAST_3DFZ_RENDER_GRAD_LIGHT',			#开启3D梯度亮度渲染模式	client.adjust_param('CONTRAST_3DFZ_RENDER_GRAD_LIGHT')
                    'contrast_3dfz_render_skeleton':'CONTRAST_3DFZ_RENDER_SKELETON',			#开启3D骨骼成像渲染模式	client.adjust_param('CONTRAST_3DFZ_RENDER_SKELETON')
                    'contrast_3dfz_skeleton_depth':'CONTRAST_3DFZ_SKELETON_DEPTH',			#开启3D骨骼深度成像	client.adjust_param('CONTRAST_3DFZ_SKELETON_DEPTH')
                    'contrast_3dfz_skeleton':'CONTRAST_3DFZ_SKELETON',			#开启3D骨骼成像	client.adjust_param('CONTRAST_3DFZ_SKELETON')
                    'contrast_3dfz_render_transp_min':'CONTRAST_3DFZ_RENDER_TRANSP_MIN',			#开启3D最小回声成像渲染模式	client.adjust_param('CONTRAST_3DFZ_RENDER_TRANSP_MIN')
                    'contrast_3dfz_render_xray':'CONTRAST_3DFZ_RENDER_XRAY',			#开启3D的X-线成像渲染模式	client.adjust_param('CONTRAST_3DFZ_RENDER_XRAY')
                    'contrast_3dfz_render_sdepth':'CONTRAST_3DFZ_RENDER_SDEPTH',			#开启3D深度成像渲染模式	client.adjust_param('CONTRAST_3DFZ_RENDER_SDEPTH')
                    'contrast_3dfz_render_slive':'CONTRAST_3DFZ_RENDER_SLIVE',			#开启3D的S-Live渲染模式	client.adjust_param('CONTRAST_3DFZ_RENDER_SLIVE')
                    'contrast_3dfz_light_pos_down':'CONTRAST_3DFZ_LIGHT_POS_DOWN',			#减小3D的灯光位置	client.adjust_param('CONTRAST_3DFZ_LIGHT_POS_DOWN')
                    'contrast_3dfz_light_pos_up':'CONTRAST_3DFZ_LIGHT_POS_UP',			#增大3D的灯光位置	client.adjust_param('CONTRAST_3DFZ_LIGHT_POS_UP')
                    'contrast_3dfz_slive_silhouette':'CONTRAST_3DFZ_SLIVE_SILHOUETTE',			#开启3D的S-Live Silhouette结构	client.adjust_param('CONTRAST_3DFZ_SLIVE_SILHOUETTE')
                    'contrast_3dfz_edit_light':'CONTRAST_3DFZ_EDIT_LIGHT',			#开启3D调节灯光功能	client.adjust_param('CONTRAST_3DFZ_EDIT_LIGHT')
                    'contrast_3dfz_slive':'CONTRAST_3DFZ_SLIVE',			#开启3D的S-Live结构	client.adjust_param('CONTRAST_3DFZ_SLIVE')
                    'contrast_3dfz_label_view':'CONTRAST_3DFZ_LABEL_VIEW',			#开启3D的视图页签	client.adjust_param('CONTRAST_3DFZ_LABEL_VIEW')
                    'contrast_3dfz_rotate_45':'CONTRAST_3DFZ_ROTATE_45',			#45度自由旋转3D成像	client.adjust_param('CONTRAST_3DFZ_ROTATE_45')
                    'contrast_3dfz_rotate_90':'CONTRAST_3DFZ_ROTATE_90',			#90度自由旋转3D成像	client.adjust_param('CONTRAST_3DFZ_ROTATE_90')
                    'contrast_3dfz_rotate_360':'CONTRAST_3DFZ_ROTATE_360',			#360度自由旋转3D成像	client.adjust_param('CONTRAST_3DFZ_ROTATE_360')
                    'contrast_3dfz_rotate_270':'CONTRAST_3DFZ_ROTATE_270',			#270度自由旋转3D成像	client.adjust_param('CONTRAST_3DFZ_ROTATE_270')
                    'contrast_3dfz_rotate_180':'CONTRAST_3DFZ_ROTATE_180',			#180度自由旋转3D成像	client.adjust_param('CONTRAST_3DFZ_ROTATE_180')
                    'contrast_3dfz_rotate_0':'CONTRAST_3DFZ_ROTATE_0',			#0度自由旋转3D成像	client.adjust_param('CONTRAST_3DFZ_ROTATE_0')
                    'contrast_3dfz_direction_top':'CONTRAST_3DFZ_DIRECTION_TOP',			#3D顶部视图	client.adjust_param('CONTRAST_3DFZ_DIRECTION_TOP')
                    'contrast_3dfz_direction_left':'CONTRAST_3DFZ_DIRECTION_LEFT',			#3D左侧视图	client.adjust_param('CONTRAST_3DFZ_DIRECTION_LEFT')
                    'contrast_3dfz_direction_fornt':'CONTRAST_3DFZ_DIRECTION_FORNT',			#3D前面视图	client.adjust_param('CONTRAST_3DFZ_DIRECTION_FORNT')
                    'contrast_3dfz_direction_back':'CONTRAST_3DFZ_DIRECTION_BACK',			#3D后面视图	client.adjust_param('CONTRAST_3DFZ_DIRECTION_BACK')
                    'contrast_3dfz_direction_right':'CONTRAST_3DFZ_DIRECTION_RIGHT',			#3D右侧视图	client.adjust_param('CONTRAST_3DFZ_DIRECTION_RIGHT')
                    'contrast_3dfz_direction_bottom':'CONTRAST_3DFZ_DIRECTION_BOTTOM',			#3D底部视图	client.adjust_param('CONTRAST_3DFZ_DIRECTION_BOTTOM')
                    'contrast_3dfz_rotatex_up':'CONTRAST_3DFZ_ROTATEX_UP',			#增大3D的X旋转角度	client.adjust_param('CONTRAST_3DFZ_ROTATEX_UP')
                    'contrast_3dfz_rotatex_down':'CONTRAST_3DFZ_ROTATEX_DOWN',			#减小3D的X旋转角度	client.adjust_param('CONTRAST_3DFZ_ROTATEX_DOWN')
                    'contrast_3dfz_rotatey_up':'CONTRAST_3DFZ_ROTATEY_UP',			#增大3D的Y旋转角度	client.adjust_param('CONTRAST_3DFZ_ROTATEY_UP')
                    'contrast_3dfz_rotatey_down':'CONTRAST_3DFZ_ROTATEY_DOWN',			#减小3D的Y旋转角度	client.adjust_param('CONTRAST_3DFZ_ROTATEY_DOWN')
                    'contrast_3dfz_rotatez_up':'CONTRAST_3DFZ_ROTATEZ_UP',			#增大3D的Z旋转角度	client.adjust_param('CONTRAST_3DFZ_ROTATEZ_UP')
                    'contrast_3dfz_rotatez_down':'CONTRAST_3DFZ_ROTATEZ_DOWN',			#减小3D的Z旋转角度	client.adjust_param('CONTRAST_3DFZ_ROTATEZ_DOWN')
                    'contrast_3dfz_moveud_up':'CONTRAST_3DFZ_MOVEUD_UP',			#3D向上移动	client.adjust_param('CONTRAST_3DFZ_MOVEUD_UP')
                    'contrast_3dfz_moveud_down':'CONTRAST_3DFZ_MOVEUD_DOWN',			#3D向下移动	client.adjust_param('CONTRAST_3DFZ_MOVEUD_DOWN')
                    'contrast_3dfz_movelr_up':'CONTRAST_3DFZ_MOVELR_UP',			#3D向右移动	client.adjust_param('CONTRAST_3DFZ_MOVELR_UP')
                    'contrast_3dfz_movelr_down':'CONTRAST_3DFZ_MOVELR_DOWN',			#3D向左移动	client.adjust_param('CONTRAST_3DFZ_MOVELR_DOWN')
                    'contrast_3dfz_label_edit':'CONTRAST_3DFZ_LABEL_EDIT',			#开启3D编辑页签	client.adjust_param('CONTRAST_3DFZ_LABEL_EDIT')
                    'contrast_3dfz_edit_rotate':'CONTRAST_3DFZ_EDIT_ROTATE',			#自由旋转3D成像	client.adjust_param('CONTRAST_3DFZ_EDIT_ROTATE')
                    'contrast_3dfz_cut_method3':'CONTRAST_3DFZ_CUT_METHOD3',			#3D方框剪切区域内部分	client.adjust_param('CONTRAST_3DFZ_CUT_METHOD3')
                    'contrast_3dfz_cut_method6':'CONTRAST_3DFZ_CUT_METHOD6',			#3D大橡皮擦剪切	client.adjust_param('CONTRAST_3DFZ_CUT_METHOD6')
                    'contrast_3dfz_cut_method5':'CONTRAST_3DFZ_CUT_METHOD5',			#3D小橡皮擦剪切	client.adjust_param('CONTRAST_3DFZ_CUT_METHOD5')
                    'contrast_3dfz_cut_method4':'CONTRAST_3DFZ_CUT_METHOD4',			#3D方框剪切区域外部分	client.adjust_param('CONTRAST_3DFZ_CUT_METHOD4')
                    'contrast_3dfz_cut_method2':'CONTRAST_3DFZ_CUT_METHOD2',			#3D描迹剪切区域外部分	client.adjust_param('CONTRAST_3DFZ_CUT_METHOD2')
                    'contrast_3dfz_cut_method1':'CONTRAST_3DFZ_CUT_METHOD1',			#3D描迹剪切区域内部分	client.adjust_param('CONTRAST_3DFZ_CUT_METHOD1')
                    'contrast_3dfz_disp_ab':'CONTRAST_3DFZ_DISP_AB',			#显示3D的AB视图	client.adjust_param('CONTRAST_3DFZ_DISP_AB')
                    'contrast_3dfz_cp_slice_b':'CONTRAST_3DFZ_CP_SLICE_B',			#选择3D的B视图进行层切	client.adjust_param('CONTRAST_3DFZ_CP_SLICE_B')
                    'contrast_3dfz_cp_slice_a':'CONTRAST_3DFZ_CP_SLICE_A',			#选择3D的A视图进行层切	client.adjust_param('CONTRAST_3DFZ_CP_SLICE_A')
                    'contrast_3dfz_disp_ac':'CONTRAST_3DFZ_DISP_AC',			#显示3D的AC视图	client.adjust_param('CONTRAST_3DFZ_DISP_AC')
                    'contrast_3dfz_cp_slice_c':'CONTRAST_3DFZ_CP_SLICE_C',			#选择3D的C视图进行层切	client.adjust_param('CONTRAST_3DFZ_CP_SLICE_C')
                    'contrast_3dfz_disp_bc':'CONTRAST_3DFZ_DISP_BC',			#显示3D的BC视图	client.adjust_param('CONTRAST_3DFZ_DISP_BC')
                    'contrast_3dfz_disp_abc':'CONTRAST_3DFZ_DISP_ABC',			#显示3D的ABC视图	client.adjust_param('CONTRAST_3DFZ_DISP_ABC')
                    'contrast_3dfz_cp_bchroma_down':'CONTRAST_3DFZ_CP_BCHROMA_DOWN',			#减小3D的B伪彩值	client.adjust_param('CONTRAST_3DFZ_CP_BCHROMA_DOWN')
                    'contrast_3dfz_cp_bchroma_up':'CONTRAST_3DFZ_CP_BCHROMA_UP',			#增大3D的B伪彩值	client.adjust_param('CONTRAST_3DFZ_CP_BCHROMA_UP')
                    'contrast_3dfz_label_mslice':'CONTRAST_3DFZ_LABEL_MSLICE',			#开启3D的断层切片页签	client.adjust_param('CONTRAST_3DFZ_LABEL_MSLICE')
                    'contrast_3dfz_ms_slice_b':'CONTRAST_3DFZ_MS_SLICE_B',			#选择3D的B切片平面	client.adjust_param('CONTRAST_3DFZ_MS_SLICE_B')
                    'contrast_3dfz_ms_slice_c':'CONTRAST_3DFZ_MS_SLICE_C',			#选择3D的C切片平面	client.adjust_param('CONTRAST_3DFZ_MS_SLICE_C')
                    'contrast_3dfz_ms_slice_a':'CONTRAST_3DFZ_MS_SLICE_A',			#选择3D的A切片平面	client.adjust_param('CONTRAST_3DFZ_MS_SLICE_A')
                    'contrast_3dfz_disp_12':'CONTRAST_3DFZ_DISP_12',			#设置3D显示模式为1*2	client.adjust_param('CONTRAST_3DFZ_DISP_12')
                    'contrast_3dfz_disp_33':'CONTRAST_3DFZ_DISP_33',			#设置3D显示模式为3*3	client.adjust_param('CONTRAST_3DFZ_DISP_33')
                    'contrast_3dfz_disp_44':'CONTRAST_3DFZ_DISP_44',			#设置3D显示模式为4*4	client.adjust_param('CONTRAST_3DFZ_DISP_44')
                    'contrast_3dfz_disp_55':'CONTRAST_3DFZ_DISP_55',			#设置3D显示模式为5*5	client.adjust_param('CONTRAST_3DFZ_DISP_55')
                    'contrast_3dfz_disp_34':'CONTRAST_3DFZ_DISP_34',			#设置3D显示模式为3*4	client.adjust_param('CONTRAST_3DFZ_DISP_34')
                    'contrast_3dfz_disp_22':'CONTRAST_3DFZ_DISP_22',			#设置3D显示模式为2*2	client.adjust_param('CONTRAST_3DFZ_DISP_22')
                    'contrast_3dfz_ms_bchroma_down':'CONTRAST_3DFZ_MS_BCHROMA_DOWN',			#减小3D断层切片的B伪彩值	client.adjust_param('CONTRAST_3DFZ_MS_BCHROMA_DOWN')
                    'contrast_3dfz_ms_bchroma_up':'CONTRAST_3DFZ_MS_BCHROMA_UP',			#增大3D断层切片的B伪彩值	client.adjust_param('CONTRAST_3DFZ_MS_BCHROMA_UP')
                    'contrast_3dfz_ms_adjustpos_down':'CONTRAST_3DFZ_MS_ADJUSTPOS_DOWN',			#微减小3D所选切片的位置	client.adjust_param('CONTRAST_3DFZ_MS_ADJUSTPOS_DOWN')
                    'contrast_3dfz_ms_adjustpos_up':'CONTRAST_3DFZ_MS_ADJUSTPOS_UP',			#微增大3D所选切片的位置	client.adjust_param('CONTRAST_3DFZ_MS_ADJUSTPOS_UP')
                    'contrast_3dfz_ms_distance_down':'CONTRAST_3DFZ_MS_DISTANCE_DOWN',			#减小3D切片间距	client.adjust_param('CONTRAST_3DFZ_MS_DISTANCE_DOWN')
                    'contrast_3dfz_ms_distance_up':'CONTRAST_3DFZ_MS_DISTANCE_UP',			#增大3D切片间距	client.adjust_param('CONTRAST_3DFZ_MS_DISTANCE_UP')
                    'contrast_3dfz_ms_slicenum_down':'CONTRAST_3DFZ_MS_SLICENUM_DOWN',			#减少3D切片数量	client.adjust_param('CONTRAST_3DFZ_MS_SLICENUM_DOWN')
                    'contrast_3dfz_ms_slicenum_up':'CONTRAST_3DFZ_MS_SLICENUM_UP',			#增多3D切片数量	client.adjust_param('CONTRAST_3DFZ_MS_SLICENUM_UP')
                    'contrast_3dfz_ms_display_down':'CONTRAST_3DFZ_MS_DISPLAY_DOWN',			#向左平移3D切片区域所有切片	client.adjust_param('CONTRAST_3DFZ_MS_DISPLAY_DOWN')
                    'contrast_3dfz_ms_display_up':'CONTRAST_3DFZ_MS_DISPLAY_UP',			#向右平移3D切片区域所有切片	client.adjust_param('CONTRAST_3DFZ_MS_DISPLAY_UP')
                    'contrast_3dfz_label_avc':'CONTRAST_3DFZ_LABEL_AVC',			#开启3D卵泡自动测量页签	client.adjust_param('CONTRAST_3DFZ_LABEL_AVC')
                    'contrast_3dfz_leftovary':'CONTRAST_3DFZ_LEFTOVARY',			#开启3D左侧卵巢	client.adjust_param('CONTRAST_3DFZ_LEFTOVARY')
                    'contrast_3dfz_rightovary':'CONTRAST_3DFZ_RIGHTOVARY',			#开启3D右侧卵巢	client.adjust_param('CONTRAST_3DFZ_RIGHTOVARY')
                    'contrast_3dfz_avc_slice_b':'CONTRAST_3DFZ_AVC_SLICE_B',			#显示卵泡3D的B视图	client.adjust_param('CONTRAST_3DFZ_AVC_SLICE_B')
                    'contrast_3dfz_avc_slice_3d':'CONTRAST_3DFZ_AVC_SLICE_3D',			#显示卵泡3D的3D图像	client.adjust_param('CONTRAST_3DFZ_AVC_SLICE_3D')
                    'contrast_3dfz_avc_slice_c':'CONTRAST_3DFZ_AVC_SLICE_C',			#显示卵泡3D的C视图	client.adjust_param('CONTRAST_3DFZ_AVC_SLICE_C')
                    'contrast_3dfz_avc_slice_a':'CONTRAST_3DFZ_AVC_SLICE_A',			#显示卵泡3D的A视图	client.adjust_param('CONTRAST_3DFZ_AVC_SLICE_A')
                    'contrast_3dfz_ms_thlow_down':'CONTRAST_3DFZ_MS_THLOW_DOWN',			#减小3D低回声阈值	client.adjust_param('CONTRAST_3DFZ_MS_THLOW_DOWN')
                    'contrast_3dfz_ms_thlow_up':'CONTRAST_3DFZ_MS_THLOW_UP',			#增大3D低回声阈值	client.adjust_param('CONTRAST_3DFZ_MS_THLOW_UP')
                    'contrast_3dfz_ms_brightness_down':'CONTRAST_3DFZ_MS_BRIGHTNESS_DOWN',			#减小3D卵泡亮度	client.adjust_param('CONTRAST_3DFZ_MS_BRIGHTNESS_DOWN')
                    'contrast_3dfz_ms_brightness_up':'CONTRAST_3DFZ_MS_BRIGHTNESS_UP',			#增大3D卵泡亮度	client.adjust_param('CONTRAST_3DFZ_MS_BRIGHTNESS_UP')
                    'contrast_3dfz_avc_volpre':'CONTRAST_3DFZ_AVC_VOLPRE',			#返回3D预激活模式	client.adjust_param('CONTRAST_3DFZ_AVC_VOLPRE')
                    # CONTRAST-4D
                    'contrast_4dpa_user_mode1':'CONTRAST_4DPA_USER_MODE1',			#开启4D第一个用户模式	client.adjust_param('CONTRAST_4DPA_USER_MODE1')
                    'contrast_4dpa_user_mode2':'CONTRAST_4DPA_USER_MODE2',			#开启4D第二个用户模式	client.adjust_param('CONTRAST_4DPA_USER_MODE2')
                    'contrast_4dpa_user_mode3':'CONTRAST_4DPA_USER_MODE3',			#开启4D第三个用户模式	client.adjust_param('CONTRAST_4DPA_USER_MODE3')
                    'contrast_4dpa_disp_full':'CONTRAST_4DPA_DISP_FULL',			#4D预激活单幅显示	client.adjust_param('CONTRAST_4DPA_DISP_FULL')
                    'contrast_4dpa_disp_dual':'CONTRAST_4DPA_DISP_DUAL',			#4D预激活双幅显示	client.adjust_param('CONTRAST_4DPA_DISP_DUAL')
                    'contrast_4dpa_disp_quad':'CONTRAST_4DPA_DISP_QUAD',			#4D预激活四幅显示	client.adjust_param('CONTRAST_4DPA_DISP_QUAD')
                    'contrast_4dpa_focus_down':'CONTRAST_4DPA_FOCUS_DOWN',			#减小4D焦点位置	client.adjust_param('CONTRAST_4DPA_FOCUS_DOWN')
                    'contrast_4dpa_focus_up':'CONTRAST_4DPA_FOCUS_UP',			#增大4D焦点位置	client.adjust_param('CONTRAST_4DPA_FOCUS_UP')
                    'contrast_4dpa_image_quality_down':'CONTRAST_4DPA_IMAGE_QUALITY_DOWN',			#减小4D图像质量	client.adjust_param('CONTRAST_4DPA_IMAGE_QUALITY_DOWN')
                    'contrast_4dpa_image_quality_up':'CONTRAST_4DPA_IMAGE_QUALITY_UP',			#增大4D图像质量	client.adjust_param('CONTRAST_4DPA_IMAGE_QUALITY_UP')
                    'contrast_4dpa_sweep_angle_down':'CONTRAST_4DPA_SWEEP_ANGLE_DOWN',			#减小4D摆动角度	client.adjust_param('CONTRAST_4DPA_SWEEP_ANGLE_DOWN')
                    'contrast_4dpa_sweep_angle_up':'CONTRAST_4DPA_SWEEP_ANGLE_UP',			#增大4D摆动角度	client.adjust_param('CONTRAST_4DPA_SWEEP_ANGLE_UP')
                    'contrast_4dpa_stalility_down':'CONTRAST_4DPA_STALILITY_DOWN',			#关闭4D稳定性	client.adjust_param('CONTRAST_4DPA_STALILITY_DOWN')
                    'contrast_4dpa_stalility_up':'CONTRAST_4DPA_STALILITY_UP',			#开启4D稳定性	client.adjust_param('CONTRAST_4DPA_STALILITY_UP')
                    'contrast_4dpa_start':'CONTRAST_4DPA_START',			#开启4D实时模式	client.adjust_param('CONTRAST_4DPA_START')
                    'contrast_4drt_render_surface':'CONTRAST_4DRT_RENDER_SURFACE',			#开启4D表面成像渲染模式	client.adjust_param('CONTRAST_4DRT_RENDER_SURFACE')
                    'contrast_4drt_edit_roi':'CONTRAST_4DRT_EDIT_ROI',			#编辑ROI锁定4D视图	client.adjust_param('CONTRAST_4DRT_EDIT_ROI')
                    'contrast_4drt_inversion':'CONTRAST_4DRT_INVERSION',			#反转4D成像	client.adjust_param('CONTRAST_4DRT_INVERSION')
                    'contrast_4drt_rotate':'CONTRAST_4DRT_ROTATE',			#自由旋转4D成像	client.adjust_param('CONTRAST_4DRT_ROTATE')
                    'contrast_4drt_disp_full':'CONTRAST_4DRT_DISP_FULL',			#4D实时单幅显示	client.adjust_param('CONTRAST_4DRT_DISP_FULL')
                    'contrast_4drt_disp_dual':'CONTRAST_4DRT_DISP_DUAL',			#4D实时双幅显示	client.adjust_param('CONTRAST_4DRT_DISP_DUAL')
                    'contrast_4drt_disp_quad':'CONTRAST_4DRT_DISP_QUAD',			#4D实时四幅显示	client.adjust_param('CONTRAST_4DRT_DISP_QUAD')
                    'contrast_4drt_orient_90':'CONTRAST_4DRT_ORIENT_90',			#90度旋转4D	client.adjust_param('CONTRAST_4DRT_ORIENT_90')
                    'contrast_4drt_orient_270':'CONTRAST_4DRT_ORIENT_270',			#270度旋转4D	client.adjust_param('CONTRAST_4DRT_ORIENT_270')
                    'contrast_4drt_reset':'CONTRAST_4DRT_RESET',			#复位4D	client.adjust_param('CONTRAST_4DRT_RESET')
                    'contrast_4drt_orient_180':'CONTRAST_4DRT_ORIENT_180',			#180度旋转4D	client.adjust_param('CONTRAST_4DRT_ORIENT_180')
                    'contrast_4drt_orient_0':'CONTRAST_4DRT_ORIENT_0',			#0度旋转4D	client.adjust_param('CONTRAST_4DRT_ORIENT_0')
                    'contrast_4drt_slice_b':'CONTRAST_4DRT_SLICE_B',			#选择4D的B视图	client.adjust_param('CONTRAST_4DRT_SLICE_B')
                    'contrast_4drt_slice_3d':'CONTRAST_4DRT_SLICE_3D',			#选择4D图像	client.adjust_param('CONTRAST_4DRT_SLICE_3D')
                    'contrast_4drt_slice_c':'CONTRAST_4DRT_SLICE_C',			#选择4D的C视图	client.adjust_param('CONTRAST_4DRT_SLICE_C')
                    'contrast_4drt_slice_a':'CONTRAST_4DRT_SLICE_A',			#选择4D的A视图	client.adjust_param('CONTRAST_4DRT_SLICE_A')
                    'contrast_4drt_threshold_down':'CONTRAST_4DRT_THRESHOLD_DOWN',			#减小4D阈值	client.adjust_param('CONTRAST_4DRT_THRESHOLD_DOWN')
                    'contrast_4drt_threshold_up':'CONTRAST_4DRT_THRESHOLD_UP',			#增大4D阈值	client.adjust_param('CONTRAST_4DRT_THRESHOLD_UP')
                    'contrast_4drt_contrast_down':'CONTRAST_4DRT_CONTRAST_DOWN',			#减小4D的对比度	client.adjust_param('CONTRAST_4DRT_CONTRAST_DOWN')
                    'contrast_4drt_contrast_up':'CONTRAST_4DRT_CONTRAST_UP',			#增大4D的对比度	client.adjust_param('CONTRAST_4DRT_CONTRAST_UP')
                    'contrast_4drt_transparency_down':'CONTRAST_4DRT_TRANSPARENCY_DOWN',			#减小4D的透明度	client.adjust_param('CONTRAST_4DRT_TRANSPARENCY_DOWN')
                    'contrast_4drt_transparency_up':'CONTRAST_4DRT_TRANSPARENCY_UP',			#增大4D的透明度	client.adjust_param('CONTRAST_4DRT_TRANSPARENCY_UP')
                    'contrast_4drt_brightness_down':'CONTRAST_4DRT_BRIGHTNESS_DOWN',			#减小4D亮度	client.adjust_param('CONTRAST_4DRT_BRIGHTNESS_DOWN')
                    'contrast_4drt_brightness_up':'CONTRAST_4DRT_BRIGHTNESS_UP',			#增大4D亮度	client.adjust_param('CONTRAST_4DRT_BRIGHTNESS_UP')
                    'contrast_4drt_smoothness_down':'CONTRAST_4DRT_SMOOTHNESS_DOWN',			#减小4D平滑值	client.adjust_param('CONTRAST_4DRT_SMOOTHNESS_DOWN')
                    'contrast_4drt_smoothness_up':'CONTRAST_4DRT_SMOOTHNESS_UP',			#增大4D平滑值	client.adjust_param('CONTRAST_4DRT_SMOOTHNESS_UP')
                    'contrast_4drt_2duscan_down':'CONTRAST_4DRT_2DUSCAN_DOWN',			#减小4D的2D微米成像值	client.adjust_param('CONTRAST_4DRT_2DUSCAN_DOWN')
                    'contrast_4drt_2duscan_up':'CONTRAST_4DRT_2DUSCAN_UP',			#增大4D的2D微米成像值	client.adjust_param('CONTRAST_4DRT_2DUSCAN_UP')
                    'contrast_4drt_3duscan_down':'CONTRAST_4DRT_3DUSCAN_DOWN',			#减小4D的3D微米成像值	client.adjust_param('CONTRAST_4DRT_3DUSCAN_DOWN')
                    'contrast_4drt_3duscan_up':'CONTRAST_4DRT_3DUSCAN_UP',			#增大4D的3D微米成像值	client.adjust_param('CONTRAST_4DRT_3DUSCAN_UP')
                    'contrast_4drt_3dchroma_down':'CONTRAST_4DRT_3DCHROMA_DOWN',			#减小4D的3D伪彩值	client.adjust_param('CONTRAST_4DRT_3DCHROMA_DOWN')
                    'contrast_4drt_3dchroma_up':'CONTRAST_4DRT_3DCHROMA_UP',			#增大4D的3D伪彩值	client.adjust_param('CONTRAST_4DRT_3DCHROMA_UP')
                    'contrast_4drt_bchroma_down':'CONTRAST_4DRT_BCHROMA_DOWN',			#减小4D的B伪彩值	client.adjust_param('CONTRAST_4DRT_BCHROMA_DOWN')
                    'contrast_4drt_bchroma_up':'CONTRAST_4DRT_BCHROMA_UP',			#增大4D的B伪彩值	client.adjust_param('CONTRAST_4DRT_BCHROMA_UP')
                    'contrast_4drt_render_grad_light':'CONTRAST_4DRT_RENDER_GRAD_LIGHT',			#开启4D梯度亮度渲染模式	client.adjust_param('CONTRAST_4DRT_RENDER_GRAD_LIGHT')
                    'contrast_4drt_render_skeleton':'CONTRAST_4DRT_RENDER_SKELETON',			#开启4D骨骼成像渲染模式	client.adjust_param('CONTRAST_4DRT_RENDER_SKELETON')
                    'contrast_4drt_skeleton_depth':'CONTRAST_4DRT_SKELETON_DEPTH',			#开启4D骨骼深度成像	client.adjust_param('CONTRAST_4DRT_SKELETON_DEPTH')
                    'contrast_4drt_skeleton':'CONTRAST_4DRT_SKELETON',			#开启4D骨骼成像	client.adjust_param('CONTRAST_4DRT_SKELETON')
                    'contrast_4drt_render_transp_min':'CONTRAST_4DRT_RENDER_TRANSP_MIN',			#开启4D最小回声成像渲染模式	client.adjust_param('CONTRAST_4DRT_RENDER_TRANSP_MIN')
                    'contrast_4drt_render_xray':'CONTRAST_4DRT_RENDER_XRAY',			#开启4D的X-线成像渲染模式	client.adjust_param('CONTRAST_4DRT_RENDER_XRAY')
                    'contrast_4drt_render_sdepth':'CONTRAST_4DRT_RENDER_SDEPTH',			#开启4D深度成像渲染模式	client.adjust_param('CONTRAST_4DRT_RENDER_SDEPTH')
                    'contrast_4drt_render_slive':'CONTRAST_4DRT_RENDER_SLIVE',			#开启4D的S-Live渲染模式	client.adjust_param('CONTRAST_4DRT_RENDER_SLIVE')
                    'contrast_4drt_light_pos_down':'CONTRAST_4DRT_LIGHT_POS_DOWN',			#减小4D的灯光位置	client.adjust_param('CONTRAST_4DRT_LIGHT_POS_DOWN')
                    'contrast_4drt_light_pos_up':'CONTRAST_4DRT_LIGHT_POS_UP',			#增大4D的灯光位置	client.adjust_param('CONTRAST_4DRT_LIGHT_POS_UP')
                    'contrast_4drt_slive_silhouette':'CONTRAST_4DRT_SLIVE_SILHOUETTE',			#开启4D的S-Live Silhouette结构	client.adjust_param('CONTRAST_4DRT_SLIVE_SILHOUETTE')
                    'contrast_4drt_edit_light':'CONTRAST_4DRT_EDIT_LIGHT',			#开启4D调节灯光功能	client.adjust_param('CONTRAST_4DRT_EDIT_LIGHT')
                    'contrast_4drt_slive':'CONTRAST_4DRT_SLIVE',			#开启4D的S-Live结构	client.adjust_param('CONTRAST_4DRT_SLIVE')
                    'contrast_4drt_label_view':'CONTRAST_4DRT_LABEL_VIEW',			#开启4D的视图页签	client.adjust_param('CONTRAST_4DRT_LABEL_VIEW')
                    'contrast_4drt_direction_top':'CONTRAST_4DRT_DIRECTION_TOP',			#4D顶部视图	client.adjust_param('CONTRAST_4DRT_DIRECTION_TOP')
                    'contrast_4drt_direction_left':'CONTRAST_4DRT_DIRECTION_LEFT',			#4D左侧视图	client.adjust_param('CONTRAST_4DRT_DIRECTION_LEFT')
                    'contrast_4drt_direction_fornt':'CONTRAST_4DRT_DIRECTION_FORNT',			#3D前面视图	client.adjust_param('CONTRAST_4DRT_DIRECTION_FORNT')
                    'contrast_4drt_direction_back':'CONTRAST_4DRT_DIRECTION_BACK',			#4D后面视图	client.adjust_param('CONTRAST_4DRT_DIRECTION_BACK')
                    'contrast_4drt_direction_right':'CONTRAST_4DRT_DIRECTION_RIGHT',			#4D右侧视图	client.adjust_param('CONTRAST_4DRT_DIRECTION_RIGHT')
                    'contrast_4drt_direction_bottom':'CONTRAST_4DRT_DIRECTION_BOTTOM',			#4D底部视图	client.adjust_param('CONTRAST_4DRT_DIRECTION_BOTTOM')
                    'contrast_4drt_rotatex_up':'CONTRAST_4DRT_ROTATEX_UP',			#增大4D的X旋转角度	client.adjust_param('CONTRAST_4DRT_ROTATEX_UP')
                    'contrast_4drt_rotatex_down':'CONTRAST_4DRT_ROTATEX_DOWN',			#减小4D的X旋转角度	client.adjust_param('CONTRAST_4DRT_ROTATEX_DOWN')
                    'contrast_4drt_rotatey_up':'CONTRAST_4DRT_ROTATEY_UP',			#增大4D的Y旋转角度	client.adjust_param('CONTRAST_4DRT_ROTATEY_UP')
                    'contrast_4drt_rotatey_down':'CONTRAST_4DRT_ROTATEY_DOWN',			#减小4D的Y旋转角度	client.adjust_param('CONTRAST_4DRT_ROTATEY_DOWN')
                    'contrast_4drt_rotatez_up':'CONTRAST_4DRT_ROTATEZ_UP',			#增大4D的Z旋转角度	client.adjust_param('CONTRAST_4DRT_ROTATEZ_UP')
                    'contrast_4drt_rotatez_down':'CONTRAST_4DRT_ROTATEZ_DOWN',			#减小4D的Z旋转角度	client.adjust_param('CONTRAST_4DRT_ROTATEZ_DOWN')
                    'contrast_4drt_moveud_up':'CONTRAST_4DRT_MOVEUD_UP',			#4D向上移动	client.adjust_param('CONTRAST_4DRT_MOVEUD_UP')
                    'contrast_4drt_moveud_down':'CONTRAST_4DRT_MOVEUD_DOWN',			#4D向下移动	client.adjust_param('CONTRAST_4DRT_MOVEUD_DOWN')
                    'contrast_4drt_movelr_up':'CONTRAST_4DRT_MOVELR_UP',			#4D向右移动	client.adjust_param('CONTRAST_4DRT_MOVELR_UP')
                    'contrast_4drt_movelr_down':'CONTRAST_4DRT_MOVELR_DOWN',			#4D向左移动	client.adjust_param('CONTRAST_4DRT_MOVELR_DOWN')
                    'contrast_4drt_label_3d4d':'CONTRAST_4DRT_LABEL_3D4D',			#开启4D的3D4D页签	client.adjust_param('CONTRAST_4DRT_LABEL_3D4D')
                    'contrast_4drt_volpre':'CONTRAST_4DRT_VOLPRE',			#返回4D预激活模式	client.adjust_param('CONTRAST_4DRT_VOLPRE')
                    }

if __name__ == '__main__':
    print('Hello world')
