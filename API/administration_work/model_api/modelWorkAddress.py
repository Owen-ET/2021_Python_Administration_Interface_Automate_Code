#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/26 10:02
# @Author  : zc
# @File    : modelWorkAddress.py

import requests
from API.administration_work.base import Base
from API.utils.functions import Functions


class ModelWorkAddress(Base):

    def searchModel(self):
        """查询接口"""

        url = self.baseUrl + self.search['url']
        data = self.search['data']
        r = self.send('POST',url,data).json()
        return r

    def addModel(self):
        """添加接口"""

        url = self.baseUrl + self.add['url']
        data = self.add['data']
        r = self.send('POST',url,data).json()
        return r

    def deleteModel(self):
        """删除接口"""

        recyclerIds = self.addModel()['data']['recyclerId']
        url = self.baseUrl + self.delete['url']
        data = str(self.delete['data'])
        dataNew = eval(data.replace("data",recyclerIds))
        r = self.send('POST',url,dataNew).json()
        return r

    def updateModel(self):
        """更新接口"""

        recyclerIds = self.addModel()['data']['recyclerId']
        url = self.baseUrl + self.update['url']
        data = str(self.update['data'])
        dataNew = eval(data.replace('data',recyclerIds))
        r = self.send('POST',url,dataNew).json()
        return r

if __name__ == '__main__':
    print(ModelWorkAddress().addModel())