# -*- coding:utf-8 -*-
# @Time : 2022/7/25 17:18
# Auther : shenyuming
# @File : task.py
# @Software : PyCharm

'''
ui的任务页面，  借助接口清除所有数据

'''
from common.baseApi import baseApi

class TaskApi(baseApi):
    pass

if __name__ == '__main__':
    from libs.api.login import LoginApi
    cookies = LoginApi().login(username='807145107@qq.com',password='123456',getcookies=True)
    TaskApi(cookies).delete_all_items()