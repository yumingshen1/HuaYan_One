# -*- coding:utf-8 -*-
# @Time : 2022/7/14 17:38
# Auther : shenyuming
# @File : organiz.py
# @Software : PyCharm
'''
部门业务类
'''
from common.baseApi import baseApi

class OrganizApi(baseApi):
    """
    添加方法--重写
    修改方法--重写
    删除全部方法--重写
    """

    def __init__(self,cookies):
        super(OrganizApi,self).__init__(cookies)    ##调用父类的init方法
        #获得总部门ID
        orgList = self.query()
        #获得第一个id
        self.top_parentID = orgList[0]['_id']
        print('部门总id:',self.top_parentID)

    def add(self,**kwargs):
        #如果是空的部门环境，就用总部门id
        if 'parent' not in kwargs:      #如果kwargs没有kwargs就用总部门id
            kwargs['parent'] = self.top_parentID
        return super(OrganizApi, self).add(**kwargs) #调用父类发送

    def update(self,id,**kwargs):
        if 'parent' not in kwargs:
            kwargs['parent'] = self.top_parentID
        return super(OrganizApi, self).update(id=id,**kwargs)

    def delete_all_items(self):
        items = self.query()[1:]      #从列表第2个取值，总部门的过滤掉
        for item in items[::-1]:        ##部门从子部门开始删除，反着循环
            self.delete(item['_id'])

if __name__ == '__main__':
    from libs.api.login import LoginApi
    cookies = LoginApi().login(username='807145107@qq.com',password='123456',getcookies=True)
    print('cookies的值：',cookies)
    ##添加部门，不带parent 参数
    # res = OrganizApi(cookies).add(name='测试部')
    # print(res)

    #查询部门列表
    # query_res = OrganizApi(cookies).query()
    # print('查询到列表的部门list：',query_res)

    ## 添加子部门 parent参数
    # OrganizApi(cookies).add(name='自动化第一部门',parent='7t5Wru7ZY5ahsmRzD')

    ##删除部门 ， 留下总部门id
    OrganizApi(cookies).delete_all_items()