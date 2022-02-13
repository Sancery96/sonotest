# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: API.py
@time: 2022/2/7 20:43
@usage: 
"""

"""
To download the vip videos, we have to use these api
this py could crawl the all api from net
"""

from urllib import request
from selenium import webdriver
from selenium.webdriver import ActionChains

if __name__ == '__main__':
    url = "https://tv.wandhi.com/go.html?url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200mxyxu2t.html"

    apis = dict()
    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    browser.get(url)
    locate = browser.find_element_by_xpath('//select')
    # simulate the behavior of the mouse click on the browser
    # only do this can load the api menu
    click = ActionChains(browser)
    click.click(locate).perform()
    # get the all api
    for locates in browser.find_elements_by_xpath('//option'):
        apis[locates.text] = locates.get_attribute('value')
        print('# @ ' + locates.get_attribute('value') + ' :' + locates.text)
