#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/05 09:11
# @Author  : zc
# @File    : base.py
import requests

from API.utils.functions import Functions


class Base:

    def __init__(self):

        self.base = Functions().getYamlData('base')
        self.add = Functions().getYamlData('add')
        self.delete = Functions().getYamlData('delete')
        self.update = Functions().getYamlData('update')
        self.search = Functions().getYamlData('search')
        self.baseUrl = self.base['baseUrl']

        self.s = requests.Session()
        self.s.headers = {
            'Authorization': f"{self.base['headers']}"
        }

    def send(self,*args,**kwargs):
        return self.s.request(*args,**kwargs)