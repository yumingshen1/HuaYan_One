# -*- coding:utf-8 -*-
# @Time : 2022/7/24 22:11
# Auther : shenyuming
# @File : basePage.py
# @Software : PyCharm
import traceback

from common.common_driver import Commdriver
from utils.handle_api_yml import get_ApiData_yml
from utils.handle_path import configs_path,screenshot_path
from configs.configs import Configs
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import strftime
from utils.handle_log import log

class basePage:
    def __init__(self):
        #打开浏览器
        self.driver = Commdriver().get_driver()
        #获取yml数据
        self.locators = get_ApiData_yml(os.path.join(configs_path,'all_elements.yml'))[self.__class__.__name__]
        for k,v in self.locators.items():
            setattr(self,k,v)   #反射，给self设置一个k属性，值v

    def open_url(self,url):
        #设置页面记载时间
        self.driver.set_page_load_timeout(Configs.set_page_load_timeout)
        self.driver.get(url)

    def get_element(self,locator,desc=None):
        try:
            return WebDriverWait(self.driver,Configs.timeout,Configs.poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            curtime = strftime('%Y%m%d%H%M%S')
            self.driver.save_screenshot(f'{screenshot_path}/{desc}{curtime}.png')
            #日志
            log.error(f'{desc}元素没有定位到')
            log.error(traceback.format_exc())  # 堆栈信息

    #获得所有元素
    def get_elements(self,locators,desc=None):
        try:
            return WebDriverWait(self.driver,Configs.timeout,Configs.poll_frequency).until(EC.visibility_of_all_elements_located(locators))
        except:
            curtime = strftime('%Y%m%d%H%M%S')
            self.driver.save_screenshot(f'{screenshot_path}/{desc}{curtime}.png')
            #日志
            log.error(f'{desc}元素没有定位到')
            log.error(traceback.format_exc()) #堆栈信息

    def input_text(self,locator,text,append=False,desc=None):
        if not append:
            self.get_element(locator,desc=desc).clear()
            self.get_element(locator,desc=desc).send_keys(text)
        else:
            self.get_element(locator,desc=desc).send_keys(text)

    def click_element(self,locator,desc=None):
        self.get_element(locator,desc=desc).click()

    def get_element_text(self,locator,desc=None):
        return self.get_element(locator,desc=desc).text

    def get_elements_test(self,locator,desc=None):
        # eles =  self.get_elements(locator,desc=desc)
        # for ele in eles:
        #     return ele.text
        return [ele.text for ele in self.get_elements(locator,desc=desc)]


    def driver_quite(self):
        self.driver.quit()
