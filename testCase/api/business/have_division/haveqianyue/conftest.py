# -*- coding:utf-8 -*-
# @Time : 2022/7/20 17:06
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm


import pytest
from libs.api.contractTypes import ContractTypesAPI
'''
有签约对象，新建签约对象
'''
@pytest.fixture(scope='session')
def init_accounts(empty_accounts,init_org):
    print('---新增签约对象初始化----')
    api_accounts = empty_accounts
    org_id = init_org[1]['_id']
    accounts_sir = api_accounts.add(name='沈sir',company_ids=[org_id])
    yield api_accounts,accounts_sir
    api_accounts.delete(accounts_sir['_id'])
    print('---新增签约对象清除---')


'''
合同类型：
清空合同类型
'''
@pytest.fixture(scope='session')
def empty_coutract_types(init_accounts):
    print('-----清空合同类型初始化---')
    #合同类型实例
    mepty_contract_type = ContractTypesAPI(init_accounts[0].cookies)
    mepty_contract_type.delete_all_items()
    yield mepty_contract_type
    print('---合同类型清除结束---')
