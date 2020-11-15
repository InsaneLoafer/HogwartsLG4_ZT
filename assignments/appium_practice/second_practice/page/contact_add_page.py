#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 20:11
# @Author   : ZhangTao
# @File     : contact_add_page.py
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from assignments.appium_practice.second_practice.page.base_page import BasePage
from assignments.appium_practice.second_practice.page.member_invite_menu import MemberInviteMenu

"""
编辑联系人
"""
class ContactAddPage(BasePage):
    def add_member(self, name, gender, phonenum):
        '''
        编辑成员信息
        '''
        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)
        self.find(MobileBy.XPATH, '//*[@text="性别"]/..//*[@text="男"]').click()
        sleep(2)
        if gender == '男':
            self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        else:
            self.find(MobileBy.XPATH, '//*[@text="女"]').click()

        # 点击输入电话号码
        self.find(MobileBy.XPATH, '//*[@text="手机号"]').send_keys(phonenum)

        # 取消勾选保存后自动发送邀请通知
        send_message = self.find(MobileBy.XPATH, '//*[@text="保存后自动发送邀请通知"]')
        if send_message.is_selected():
            send_message.click()

        # 点击保存
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()

        return MemberInviteMenu(self.driver)
