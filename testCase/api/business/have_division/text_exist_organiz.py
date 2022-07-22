# -*- coding:utf-8 -*-
# @Time : 2022/7/18 15:50
# Auther : shenyuming
# @File : text_exist_organiz.py
# @Software : PyCharm
'''
有子部门情况基础上，添加部门
'''
import pytest

from common.ApiAssert import ApiAssert

@pytest.fixture()
def tc0002_fixtrue(init_org):
    print('--test_tc0002数初始化---')
    api_org= init_org[0]
    yield api_org
    api_org.delete(org['_id'])
    print('---test_tc0002数据清除完成---')


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


'''
当前已有子部门情况下，修改部门
'''

@pytest.fixture()
def tc00051_fixtrue(init_org):
    print('---tc0005数据初始化----')
    api_org = init_org[0]
    new_org = api_org.add(name='产品部门')
    yield api_org,new_org
    api_org.delete(new_org['_id'])
    print('---tc0005数据清除----')


def test_tc00051(tc00051_fixtrue):
    api_org,new_org = tc00051_fixtrue
    #修改部门
    api_org.update(new_org['_id'],name='运维部门')
    list_org = api_org.query()
    #断言
    for org in list_org:
        if org['_id'] == new_org['_id']:    #找对应的部门id
            ApiAssert.api_Assert('运维部门','==',org['name'])



if __name__ == '__main__':
    pytest.main([__file__,'-s','-k','0005'])