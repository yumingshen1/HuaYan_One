# -*- coding:utf-8 -*-
# @Time : 2022/7/14 17:27
# Auther : shenyuming
# @File : login.py
# @Software : PyCharm
from common.baseApi import baseApi

class LoginApi(baseApi):

    ##内部函数，处理登录参数，
    def __creat_data(self,username,password):
        return {"user":{"email":username},"password":password,"code":"","locale":"zh- cn"}


    def login(self,username,password,getcookies=False):

            payload = self.__creat_data(username,password)
            respData = self.request_send("POST",json=payload,isLogin=True)
            if getcookies:
                return respData.cookies
            else:
                return respData


if __name__ == '__main__':
    res = LoginApi().login(username='807145107@qq.com',password='123456',getcookies=True)
    print(res)