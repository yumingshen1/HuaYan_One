# -*- coding:utf-8 -*-
# @Time : 2022/7/25 15:32
# Auther : shenyuming
# @File : taskPage.py
# @Software : PyCharm

from common.basePage import basePage

class TaskPage(basePage):
    #添加新任务
    def add_new_task(self,summary_name,date):
        #新建
        self.click_element(self.new_btn)
        #主题
        self.input_text(self.summary_input,summary_name)
        #日期
        self.input_text(self.select_date,date)
        #保存
        self.click_element(self.save_btn)

    #返回列表
    def back_task_list(self):
        self.click_element(self.task_tab)

    #获取任务名称
    def get_task_names(self):
        return self.get_elements_test(self.task_list)


