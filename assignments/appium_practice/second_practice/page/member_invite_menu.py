#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 16:49
# @Author   : ZhangTao
# @File     : member_invite_menu.py
# 添加成员页
from appium.webdriver.common.mobileby import MobileBy
from assignments.appium_practice.second_practice.page.base_page import BasePage


class MemberInviteMenu(BasePage):
    def add_member_manul(self):
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()

        from assignments.appium_practice.second_practice.page.contact_add_page import ContactAddPage
        return ContactAddPage(self.driver)

