# -*- coding:utf-8 -*-
# @Time : 2022/7/21 12:45
# Auther : shenyuming
# @File : test_exist_contract_type.py
# @Software : PyCharm

import pytest
from common.ApiAssert import ApiAssert
'''
合同分类
有合同分类基础上，再添加合同分类
'''

@pytest.fixture()
def tc002002_fixtrue(init_contract_types):
    print('---tc002002初始化---')
    #获得实例
    api_contract_type = init_contract_types[0]
    yield api_contract_type
    api_contract_type.delete(contract_type['_id'])
    print('---tc002002清除----')


def test_tc002002(tc002002_fixtrue):
    global contract_type
    api_contract_type = tc002002_fixtrue
    contract_type = api_contract_type.add(name='房屋转让合同11')
    list_contract = api_contract_type.query()
    ApiAssert.api_Assert(contract_type,'in',list_contract)

if __name__ == '__main__':
    pytest.main([__file__,'-sv'])