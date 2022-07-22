# -*- coding:utf-8 -*-
# @Time : 2022/7/14 18:19
# Auther : shenyuming
# @File : handle_api_yml.py
# @Software : PyCharm
import os

from utils.handle_path import product_path,configs_path,caseData_path
import yaml

def get_ApiData_yml(fileDir):
    with open(fileDir,'r',encoding='utf-8') as f:
        return yaml.safe_load(f.read())


# [(),()] 参数化格式
def get_yml_caseData(fileDir,caseName):
    content = get_ApiData_yml(fileDir)[caseName]
    test_data = list(content.values())      #获得字典值
    print(test_data)
    res = list(zip(*test_data))      # @zip,  *解包为两个list， zip打包到一起
    print(res)
    return res


if __name__ == '__main__':
    fileDir = os.path.join(caseData_path,'contract_data.yml')
    get_yml_caseData(fileDir,'test_tc003001')