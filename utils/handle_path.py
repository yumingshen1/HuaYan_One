# -*- coding:utf-8 -*-
# @Time : 2022/7/14 18:03
# Auther : shenyuming
# @File : handle_path.py
# @Software : PyCharm

import os

##工程路径
product_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

##configs
configs_path = os.path.join(product_path,'configs')

if __name__ == '__main__':

    print(configs_path)