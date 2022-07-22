# -*- coding:utf-8 -*-
# @Time : 2022/7/22 12:00
# Auther : shenyuming
# @File : test_contracts.py
# @Software : PyCharm

'''
合同数据
'''
import pytest,os
from common.ApiAssert import ApiAssert
from utils.handle_path import caseData_path
from utils.handle_api_yml import get_yml_caseData

@pytest.fixture()
def tc003001_fixtrue(empty_contracts):
    print('tc003001数据初始化')
    api_contract = empty_contracts
    yield api_contract
    api_contract.delete(contract['_id'])
    print('tc003001数据清除')

@pytest.mark.parametrize('name,amount',get_yml_caseData(os.path.join(caseData_path,'contract_data.yml'),'test_tc003001'))
def test_tc003001(tc003001_fixtrue,init_accounts,init_contract_types,init_org,name,amount):
    global contract
    api_contract = tc003001_fixtrue
    contract = api_contract.add(othercompany = init_accounts[1]['_id'],
                     contract_type=init_contract_types[1]['_id'],
                     name=name,
                     company_id=init_org[1]['_id'],
                     amount=amount)
    list_contracts = api_contract.query()
    ApiAssert.api_Assert(contract,'in',list_contracts)

if __name__ == '__main__':
    pytest.main([__file__,'-sv'])