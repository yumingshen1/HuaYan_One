# -*- coding:utf-8 -*-
# @Time : 2022/7/18 12:52
# Auther : shenyuming
# @File : test_organiz.py
# @Software : PyCharm

import pytest
from common.ApiAssert import ApiAssert

'''
test_tc0001 用例自己的初始化和清除
'''
@pytest.fixture()
def tc0001_fixtrue(empty_orgs):
    print('---test_tc0001数据初始化----')
    api_org = empty_orgs      ##获得部门实例
    yield api_org
    api_org.delete(org['_id'])  ##清除数据
    print('---test_tc0001数据清除完成---')


def test_tc0001(tc0001_fixtrue):

    global org  #全局设置变量，用于清除数据

    #tc0001_fixtrue中获得实例
    api_org = tc0001_fixtrue
    #添加一个部门
    org = api_org.add(name='测试部门')
    #l列出所有部门
    list_org = api_org.query()
    #断言
    ApiAssert.api_Assert(org,'in',list_org)

if __name__ == '__main__':
    pytest.main([__file__,'-s'])