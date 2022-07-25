# -*- coding:utf-8 -*-
# @Time : 2022/7/24 21:59
# Auther : shenyuming
# @File : common_driver.py
# @Software : PyCharm

from selenium import webdriver
from configs.configs import Configs

#单例
class Single:
    def __new__(cls, *args, **kwargs):
        #重写new方法
        if not hasattr(cls,"_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

class Commdriver(Single):
    driver = None
    def get_driver(self,browser_name=Configs.browser_name,handless_flage=Configs.handless_flage):
        if self.driver is None:
            if not handless_flage:
                if browser_name == 'chrome':
                    self.driver = webdriver.Chrome()
                elif browser_name == 'firefox':
                    self.driver = webdriver.Firefox()
                else:
                    raise ValueError(f'不支持的浏览器{browser_name}')

            else:
                if browser_name == 'chrome':
                    _options = webdriver.ChromeOptions()
                    _options.add_argument('--headless')
                    self.driver = webdriver.Chrome(options=_options)
                elif browser_name == 'firefox':
                    _options = webdriver.ChromeOptions()
                    _options.add_argument('--headless')
                    self.driver = webdriver.Chrome(options=_options)
                else:
                    raise ValueError(f'不支持的浏览器{browser_name}')
            self.driver.maximize_window()
            self.driver.implicitly_wait(Configs.implicitly_wait)
        return self.driver

if __name__ == '__main__':
    Commdriver().get_driver()
