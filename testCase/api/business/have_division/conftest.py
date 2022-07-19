# -*- coding:utf-8 -*-
# @Time : 2022/7/18 15:46
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm
import pytest

@pytest.fixture(scope='session')
def init_org(empty_orgs):
    ##获取部门实例
    api_org = empty_orgs
    print('---新增部门初始化---')
    org = api_org.add(name='研发部')
    yield api_org
    api_org.delete(org['_id'])
    print('---新增部门清除完成---')
