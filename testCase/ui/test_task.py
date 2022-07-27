# -*- coding:utf-8 -*-
# @Time : 2022/7/25 17:39
# Auther : shenyuming
# @File : test_task.py
# @Software : PyCharm

'''
任务用例
'''
import pytest,os,allure
from common.ApiAssert import ApiAssert
from utils.handle_path import caseData_path,report_path
from utils.handle_api_yml import get_yml_caseData
from utils.handle_date import get_date_str

@allure.epic('华焱项目——task——UI')
@allure.feature('task任务')
@allure.story('task任务添加')
@allure.title('{title}')
@pytest.mark.usefixtures('task_fixtrue')
@pytest.mark.parametrize('title,summary,date',get_yml_caseData(os.path.join(caseData_path,'task_test_data.yml'),'test_task'))
def test_task(login_init,title,summary,date):
    main_page = login_init
    #进入任务页面
    task_page = main_page.goto_TaskPage()
    #处理日期格式
    input_date = get_date_str(date)
    #新建任务
    task_page.add_new_task(summary,input_date)
    #列出任务
    task_page.back_task_list()
    #获取所有任务名称
    list_task_name = task_page.get_task_names()
    ApiAssert.api_Assert(summary,'in',list_task_name)


if __name__ == '__main__':
    pytest.main([__file__,'-sv','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')
