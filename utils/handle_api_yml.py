# -*- coding:utf-8 -*-
# @Time : 2022/7/14 18:19
# Auther : shenyuming
# @File : handle_api_yml.py
# @Software : PyCharm
import os

from utils.handle_path import product_path,configs_path
import yaml

def get_ApiData_yml(fileDir):
    with open(fileDir,'r',encoding='utf-8') as f:
        return yaml.safe_load(f.read())


if __name__ == '__main__':
    fileDir = os.path.join(configs_path,'apiConfig.yml')
    print(get_ApiData_yml(fileDir=fileDir))