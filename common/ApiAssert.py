# -*- coding:utf-8 -*-
# @Time : 2022/7/17 21:28
# Auther : shenyuming
# @File : ApiAssert.py
# @Software : PyCharm

from typing import Iterable

class ApiAssert:
    @classmethod
    def api_Assert(cls,result,condition,exp_result):
        try:
            assert_type = {
                "==":result == exp_result,
                "!=":result != exp_result,
                    ##in， not in 是序列， 判断exp_result是不是可迭代序列，是就校验，不是返回false
                "in":result in exp_result if isinstance(exp_result,Iterable) else False,
                "not in":result not in exp_result if isinstance(exp_result,Iterable) else False
            }
            if condition in assert_type:
                assert assert_type[condition]
            else:
                raise AssertionError('请输入正确的断言情况')

        except Exception as error:
            #日志
            raise error

if __name__ == '__main__':
    ApiAssert.api_Assert(5,'in',(1,3,5))