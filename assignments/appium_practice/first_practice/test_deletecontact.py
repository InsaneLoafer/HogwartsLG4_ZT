#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 11:09
# @Author   : ZhangTao
# @File     : test_deletecontact.py
from time import sleep
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .base import Base

class TestDeleteContact(Base):
    def setup(self):
        self.caps()

    def teardown(self):
        self.driver.quit()

    def find_name(self, name):
        # 点击放大镜按钮
        self.fXpath('//*[@resource-id="com.tencent.wework:id/i6n"]').click()

        # 点击搜索输入框输入内容
        self.fXpath('//*[@text="搜索"]').send_keys(name)
        sleep(2)

    def get_nameList(self, name):
        # 获取搜索结果列表
        # resultlist = self.fXpaths('//*[@resource-id="com.tencent.wework:id/bwn"]')
        resultlist = self.fXpaths(f'//*[@text="{name}"]')
        sleep(2)

        print(len(resultlist))
        return len(resultlist)

    @pytest.mark.parametrize("name", ["aa11", "aa12"])
    def test_deletecontact(self, name):
        # 打开通讯录
        self.open_contact()

        # 获取初始列表
        self.find_name(name)
        original_list = self.get_nameList(name)

        # 点击要删除的人
        self.fXpath('//*[@resource-id="com.tencent.wework:id/bwn"]').click()

        # 点击右上角三个点
        self.driver.find_element_by_id('com.tencent.wework:id/i6d').click()

        # 点击编辑成员
        self.fXpath('//*[@text="编辑成员"]').click()

        # 点击删除成员
        self.fXpath('//*[@text="删除成员"]').click()

        # 点击确定
        self.fXpath('//*[@text="确定"]').click()

        # 获取删除后的列表
        sleep(2)
        deleted_list = self.get_nameList(name)

        # 判断删除后的列表长度是否减一
        assert original_list - deleted_list == 1


        # 另一种判断方法：获取提示
        # sleep(2)
        # result = self.fXpath('//*[@text="无搜索结果"]').text
        # print(result)
        # assert result == "无搜索结果"

