# -*- coding:utf-8 -*-
# @Time : 2022/7/18 15:46
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm
import pytest

'''
登录后新增部门，清除部门，  新增一个部门用于测试环境
'''
@pytest.fixture(scope='session')
def init_org(empty_orgs):
    ##获取部门实例
    api_org = empty_orgs
    print('---新增部门初始化---')
    org = api_org.add(name='研发部')
    yield api_org,org
    api_org.delete(org['_id'])
    print('---新增部门清除完成---')


'''
签约对象
有部门
清空签约对象
'''
from libs.api.accounts import AccountsAPI

@pytest.fixture(scope='session')
def empty_accounts(init_org):
    print('----签约对象初始化开始----')
    api_accounts = AccountsAPI(init_org[0].cookies)    ##实例化后，从上层拿到cookies
    api_accounts.delete_all_items()         ##清空所有的签约对象
    yield api_accounts
    print('---清空签约对象结束----')