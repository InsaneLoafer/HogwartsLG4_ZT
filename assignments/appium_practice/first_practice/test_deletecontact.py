#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 11:09
# @Author   : ZhangTao
# @File     : test_deletecontact.py
import pytest
from .base import Base


class TestDeleteContact(Base):
    def setup(self):
        self.setup()

    def teardown(self):
        self.teardown()

    def find_name(self, name):
        # 点击放大镜按钮
        self.fXpath('//*[@resource-id="com.tencent.wework:id/i6n"]').click()

        # 点击搜索输入框
        self.fXpath('//*[@resource-id="com.tencent.wework:id/gpg"]').send_keys(name)

        # 获取搜索结果列表
        resultlist = self.fXpaths('//android.widget.FrameLayout')[5:]
        return len(resultlist)

    @pytest.mark.parametrize('name', ['12', 'michael72121', 'michael69227'])
    def test_deletecontact(self, name):
        # 打开通讯录
        self.open_contact()

        # 获取初始列表
        original_list = self.find_name(name)

        # 选择要删除的人
        self.scroll_find(name)

        # 点击右上角三个点
        self.fXpath('//*[resource-id="com.tencent.wework:id/i6d"]').click()

        # 点击编辑成员
        self.fXpath('//*[@text="编辑成员"]').click()

        # 点击删除成员
        self.fXpath('//*[@text="删除成员"]').click()

        # 点击确定
        self.fXpath('//*[@text="确定"]').click()

        # 获取删除后的列表
        deleted_list = self.find_name(name)

        # 判断删除后的列表长度是否减一
        assert original_list - deleted_list == 1


