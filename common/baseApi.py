# -*- coding:utf-8 -*-
# @Time : 2022/7/12 21:11
# Auther : shenyuming
# @File : baseApi.py
# @Software : PyCharm

import requests,os
from utils.handle_api_yml import get_ApiData_yml
from utils.handle_path import configs_path
from configs.configs import Configs

class baseApi:
    def __init__(self,cookies=None):
        '''
        1,获取配置信息：path,port,请求体，请求方式
        2，业务接口的cookies，token
        '''
        if cookies:
            self.cookies = cookies
            self.spaceid = self.cookies['X-Space-Id']
        else:
            self.cookies = None

        #获得配置文件数据
        self.data = get_ApiData_yml(os.path.join(configs_path,'apiConfig.yml'))[self.__class__.__name__]

    def request_send(self,method,json=None,params=None,id="",isLogin=False):

        PATH = self.data['path']
        # method = self.data['Method']
        try:
            resp = requests.request(method,url=f'{Configs.HOST}{PATH}/{id}',json=json,params=params,cookies=self.cookies)

            if isLogin:     #登录返回响应体，其他的返回json数据
                return resp
            return resp.json()
        except Exception as e:
            raise e

    def add(self,**kwargs):
        """
        :param kwargs: 业务不一样，使用不定参数 ； 替换数据space ；
        :return:
        """
        payload = self.data['add']
        kwargs['space'] = self.spaceid
        payload.update(kwargs)

        resp = self.request_send('POST',json=payload)
        #过滤
        return resp['value'][0]

    def delete(self,id):
        """
        :param id:  部门id
        :return: resp相应数据
        """
        return self.request_send('DELETE',id=id)

    def update(self,id,**kwargs):
        """
        :param id: 修改的部门id
            kwargs:  可能有需要替换的数据
        :return:
        """
        payload = self.data['update']
        kwargs['space'] = self.spaceid
        payload['$set'].update(kwargs)

        resp = self.request_send(id=id,json=payload)
        return resp



    def query(self,**kwargs):
        """
        :param kwargs: 参数，  **kwargs----》params参数
        :return: resp['value']
        """
        resp = self.request_send('GET',params=kwargs)
        return resp['value']

    def delete_all_items(self):
        """
        1,一般在fixture中
        2，查询所有数据，根据循环删除
            某些不能删除， 需要在业务类重写
        :return:
        """
        ##查询所有数据
        items = self.query()
        ##循环删除
        for item in items:
            self.delete(item['_id'])