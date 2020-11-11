#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/11 10:34
# @Author   : ZhangTao
# @File     : test_addcontact.py
from time import sleep

import allure
import pytest
from .base import Base

# @allure.feature('测试企业微信添加联系人')
class TestAddContact(Base):
    def setup(self):
        self.caps()

    def teardown(self):
        self.driver.quit()

    # @allure.story('添加联系人测试')
    @pytest.mark.parametrize(['name', 'gender', 'phone'],[
                             ['aa11', '男', '13311112222'],
                             ['aa12', '女', '13311112223']])
    def test_addcontact(self, name, gender, phone):
        # 打开通讯录
        # with allure.story('打开通讯录'):
        self.open_contact()

        # 滑动点击添加成员
        # with allure.story('添加成员'):
        self.scroll_find("添加成员")

        # 点击手动输入添加
        self.fXpath('//*[@text="手动输入添加"]').click()

        # 点击输入姓名
        # with allure.story('输入姓名'):
        self.fXpath('//*[contains(@text,"姓名")] /../ android.widget.EditText').send_keys(name)

        # 选择性别
        # with allure.story('选择性别'):
        self.fXpath('//*[@text="性别"]/..//*[@text="男"]').click()
        sleep(2)
        if gender == '男':
            self.fXpath('//*[@text="男"]').click()
        else:
            self.fXpath('//*[@text="女"]').click()

        # 点击输入电话号码
        # with allure.story('输入电话号码'):
        # self.fXpath('//*[contains(@text,"姓名")] /../ android.widget.EditText').send_keys(phone)
        self.fXpath('//*[@text="手机号"]').send_keys(phone)

        # 取消勾选保存后自动发送邀请通知
        send_message = self.fXpath('//*[@text="保存后自动发送邀请通知"]')
        if send_message.is_selected():
            send_message.click()

        # 点击保存
        # with allure.story('点击保存'):
        self.fXpath('//*[@text="保存"]').click()

        # 获取toast文本
        # with allure.story('获取toast'):
        result = self.fXpath('//*[@class="android.widget.Toast"]').text
        assert result == '添加成功'

