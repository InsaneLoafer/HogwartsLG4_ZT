#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/2 20:50
# @Author   : ZhangTao
# @File     : test_data.py
import pytest
import yaml

class TestData:
    @pytest.mark.parametrize(["a","b"],[
        (10,20),
        (10,2),
        (3,9)
    ])
    def test_data(self, a, b):
        print(a+b)

    # 利用yaml文件参数化
    @pytest.mark.parametrize(["a","b"], yaml.safe_load(open("./data.yaml")))
    def test_data1(self, a, b):
        print(a+b)

