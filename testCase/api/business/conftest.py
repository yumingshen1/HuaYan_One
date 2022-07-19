# -*- coding:utf-8 -*-
# @Time : 2022/7/18 12:40
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm

import pytest
from libs.api.login import LoginApi
from libs.api.organiz import OrganizApi

##登录初始化
@pytest.fixture(scope='session',autouse=False)
def login_init():
    print('----登录初始化-----')
    cookies = LoginApi().login(username='807145107@qq.com',password='123456',getcookies=True)
    yield cookies


##清空部门
@pytest.fixture(scope='session')
def empty_orgs(login_init):
    print('----开始清除部门数据----')
    cookies = login_init
    org = OrganizApi(cookies)
    org.delete_all_items()
    yield org
    print('----部门数据清除完成----')