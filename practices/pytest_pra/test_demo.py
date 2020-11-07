#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/2 21:11
# @Author   : ZhangTao
# @File     : test_demo.py
import pytest
import yaml

"""
yaml文件内容如果有字典，需要加上-来转化为列表才能打印出其key:value
如下所示：
-
  test: 127.0.0.1
"""
class TestDemo:
    @pytest.mark.parametrize('env', yaml.safe_load(open("./env.yaml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的ip是：", env["test"])

        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的ip是：", env["dev"])