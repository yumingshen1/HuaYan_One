# -*- coding:utf-8 -*-
# @Time : 2022/7/21 11:58
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm

'''
合同类型
先清空合同类型 在新增合同类型，之后再基础上添加合同类型
'''
import pytest
from libs.api.contracts import ContractsAPI
@pytest.fixture(scope='session')
def init_contract_types(empty_coutract_types):
    print('---新增房屋合同类型初始化----')
    api_contract_type = empty_coutract_types
    contract_type = api_contract_type.add(name='租赁合同')
    yield api_contract_type,contract_type
    api_contract_type.delete(contract_type['_id'])
    print('---新增房屋合同类型清除----')


'''
合同数据清理
'''
@pytest.fixture(scope='session')
def empty_contracts(init_contract_types):
    print('----合同数据初始化----')
    #获得合同数据实例
    api_contract = ContractsAPI(init_contract_types[0].cookies)
    api_contract.delete_all_items()
    yield api_contract
    print('---合同数据清除完成----')
