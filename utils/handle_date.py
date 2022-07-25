# -*- coding:utf-8 -*-
# @Time : 2022/7/25 20:36
# Auther : shenyuming
# @File : handle_date.py
# @Software : PyCharm

import arrow        #arrow 处理日期

def get_date_str(date_str):
    if date_str == 'today':
        return arrow.now().format('YYYY-MM-DD')
    elif date_str == 'tomrrow':
        return arrow.now().shift(days=1).format('YYYY-MM-DD')
    elif date_str.endswith('days later'):
        date_num = int(date_str.split(' ')[0])
        return arrow.now().shift(days=date_num).format('YYYY-MM-DD')
    else:
        return ValueError(f'没有匹配的规则{date_str}')

if __name__ == '__main__':
    print(get_date_str('10 days later'))