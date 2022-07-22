# -*- coding:utf-8 -*-
# @Time : 2022/7/20 15:59
# Auther : shenyuming
# @File : test_accounts.py
# @Software : PyCharm

'''
有部门的无签约对象时，新增签约对象用例
'''
import pytest
from common.ApiAssert import ApiAssert

@pytest.fixture
def tc001001_fixtrue(empty_accounts):
    print('----tc001001初始化开始-----')
    api_accounts = empty_accounts
    yield api_accounts
    api_accounts.delete(account['_id'])
    print('----tc001001清除数据----')

def test_tc001001(tc001001_fixtrue,init_org):
    global account
    api_accounts = tc001001_fixtrue
    #获取部门id
    org_id = init_org[1]['_id']
    #添加签约对象
    account = api_accounts.add(name='沈总',company_ids=[org_id])
    list_accounts = api_accounts.query()
    ApiAssert.api_Assert(account,'in',list_accounts)


if __name__ == '__main__':
    pytest.main([__file__,'-sv'])