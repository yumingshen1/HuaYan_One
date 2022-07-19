# -*- coding:utf-8 -*-
# @Time : 2022/7/18 15:50
# Auther : shenyuming
# @File : text_exist_organiz.py
# @Software : PyCharm
import pytest

from common.ApiAssert import ApiAssert

@pytest.fixture()
def tc0002_fixtrue(init_org):
    print('--test_tc0002数初始化---')
    api_org= init_org
    yield api_org
    api_org.delete(org['_id'])


def test_tc0002(tc0002_fixtrue):
    global org
    ##获得部门实例
    api_org = tc0002_fixtrue
    ##添加部门
    org = api_org.add(name='一部门')
    ##获得列表
    list_org = api_org.query()
    #断言
    ApiAssert.api_Assert(org,'in',list_org)

if __name__ == '__main__':
    pytest.main([__file__,'-s'])