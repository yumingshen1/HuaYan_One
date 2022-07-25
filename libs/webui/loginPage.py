# -*- coding:utf-8 -*-
# @Time : 2022/7/25 14:24
# Auther : shenyuming
# @File : loginPage.py
# @Software : PyCharm

from common.basePage import basePage
from libs.webui.mainPage import MainPage

class LoginPage(basePage):
    def open_login_page(self,url):
        self.open_url(url)
        return self

    def login(self,username,password):
        self.input_text(self.email_input,username)
        self.input_text(self.psw_input,password)
        self.click_element(self.login_btn)
        return MainPage()


if __name__ == '__main__':
    LoginPage().open_login_page('http://124.223.33.41:7070/').login('807145107@qq.com','123456')