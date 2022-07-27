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

#casedata
caseData_path = os.path.join(product_path,'data')

#screenshot
screenshot_path = os.path.join(product_path,'outFiles/screenshot')

#日志
logs_path = os.path.join(product_path,'outFiles/logs')

#报告
report_path = os.path.join(product_path,'outFiles/report')

if __name__ == '__main__':

    print(screenshot_path)