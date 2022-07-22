# -*- coding:utf-8 -*-
# @Time : 2022/7/21 11:40
# Auther : shenyuming
# @File : test_contract_type.py
# @Software : PyCharm

import pytest
from common.ApiAssert import ApiAssert
'''
清空合同类型后 在添加合同类型用例
'''

@pytest.fixture()
def tc002001_fixtrue(empty_coutract_types):
    print('----tc002001数据初始化----')
    #和同实例
    api_contract_type = empty_coutract_types
    yield api_contract_type
    api_contract_type.delete(contract['_id'])
    print('---tc002001数据清除---')


def test_tc002001(tc002001_fixtrue):
    global contract
    api_contract_type = tc002001_fixtrue
    contract = api_contract_type.add(name='房屋买卖合同类型')
    list_contract_type = api_contract_type.query()
    ApiAssert.api_Assert(contract,'in',list_contract_type)

if __name__ == '__main__':
    pytest.main([__file__,'-sv'])