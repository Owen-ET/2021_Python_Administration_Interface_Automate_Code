#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/26 09:55
# @Author  : zc
# @File    : test_model.py

import allure
from API.test_case.base_testcase import BaseTestCase

@allure.feature('执行以下测试用例：')
class TestModel(BaseTestCase):

    @allure.story('测试用例1：查询接口')
    def test_searchModel(self):

        result = self.model.searchModel()
        assert 200 == result['code'],"与预想结果不对！"

    @allure.story('测试用例1：添加接口')
    def test_addModel(self):

        result = self.model.addModel()
        assert 200 == result['code'],"与预想结果不对！"

    @allure.story('测试用例1：删除接口')
    def test_deleteModel(self):

        result = self.model.deleteModel()
        assert 200 == result['code'],"与预想结果不对！"

    @allure.story('测试用例1：更新接口')
    def test_updateModel(self):

        result = self.model.updateModel()
        assert 200 == result['code'], "与预想结果不对！"