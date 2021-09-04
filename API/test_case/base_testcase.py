#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/26 09:47
# @Author  : zc
# @File    : base_testcase.py

from API.administration_work.model_api.modelWorkAddress import ModelWorkAddress


class BaseTestCase:

    def setup(self):
        print("=======start=======")
        self.model = ModelWorkAddress()

    def teardown(self):
        print("=======stop=======")