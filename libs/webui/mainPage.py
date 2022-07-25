# -*- coding:utf-8 -*-
# @Time : 2022/7/25 15:30
# Auther : shenyuming
# @File : mainPage.py
# @Software : PyCharm
from common.basePage import basePage
from libs.webui.pageObjects.taskPage import TaskPage

class MainPage(basePage):
    def goto_TaskPage(self):
        self.click_element(self.task_tab)
        return TaskPage()