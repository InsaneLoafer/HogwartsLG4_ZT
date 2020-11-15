#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 21:04
# @Author   : ZhangTao
# @File     : contact_detail_page.py
from appium.webdriver.common.mobileby import MobileBy
from assignments.appium_practice.second_practice.page.base_page import BasePage
from assignments.appium_practice.second_practice.page.contact_setting_page import ContactSetting


class ContactDetailPage(BasePage):
    def goto_contact_setting(self):
        # 点击右上角三个点
        self.find(MobileBy.ID, 'com.tencent.wework:id/i6d').click()
        return ContactSetting(self.driver)