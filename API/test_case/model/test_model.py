#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/08/26 09:55
# @Author  : zc
# @File    : test_model.py


from API.test_case.base_testcase import BaseTestCase


class TestModel(BaseTestCase):

    def test_searchModel(self):

        result = self.model.searchModel()
        assert 2001 == result['code'],"与预想结果不对！"

    def test_addModel(self):

        result = self.model.addModel()
        assert 200 == result['code'],"与预想结果不对！"

    def test_deleteModel(self):

        result = self.model.deleteModel()
        assert 200 == result['code'],"与预想结果不对！"

    def test_updateModel(self):

        result = self.model.updateModel()
        assert 200 == result['code'], "与预想结果不对！"