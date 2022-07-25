# -*- coding:utf-8 -*-
# @Time : 2022/7/25 17:22
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm

'''
登录到主页面
清空搜有任务
'''

import pytest
from libs.webui.loginPage import LoginPage
from configs.configs import Configs
from libs.api.login import LoginApi
from libs.api.task import TaskApi

@pytest.fixture(scope='session')
def login_init():
    print('----登录初始化----')
    main_page = LoginPage().open_login_page(Configs.HOST).login(Configs.usernam,Configs.password)
    yield main_page
    main_page.driver_quite()
    print('---关闭浏览器----')


@pytest.fixture(scope='session')
def task_fixtrue():
    print('---清空任务初始化---')
    cookies = LoginApi().login(username='807145107@qq.com',password='123456',getcookies=True)
    task_data = TaskApi(cookies)
    task_data.delete_all_items() #测试前 清除
    yield
    # task_data.delete_all_items() #测试完清除