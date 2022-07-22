# -*- coding:utf-8 -*-
# @Time : 2022/7/20 17:07
# Auther : shenyuming
# @File : test_exist_accounts.py
# @Software : PyCharm
'''
有签约对象，新建签约对象用例
'''
import pytest
from common.ApiAssert import ApiAssert

@pytest.fixture()
def tc001002_fixtrue(init_accounts):
    print('----tc001002初始化---')
    api_accounts = init_accounts[0]
    yield api_accounts
    api_accounts.delete(account['_id'])
    print('tc001002清除数据---')


def test_tc001002(tc001002_fixtrue,init_org):
    global account
    #签约对象
    api_accounts = tc001002_fixtrue
    #部门id
    org_id = init_org[1]['_id']
    #添加签约对象
    account = api_accounts.add(name='沈董事',company_ids=[org_id])
    #列出签约对象
    list_accounts = api_accounts.query()
    ApiAssert.api_Assert(account,'in',list_accounts)

if __name__ == '__main__':
    pytest.main([__file__,'-sv'])