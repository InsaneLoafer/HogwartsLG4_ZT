#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 13:50
# @Author   : ZhangTao
# @File     : contact_list_page.py

# 通讯录
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from assignments.appium_practice.second_practice.page.base_page import BasePage
from assignments.appium_practice.second_practice.page.contact_detail_page import ContactDetailPage


class ContactListPage(BasePage):

    def goto_member_invite_menu(self):
        # 点击添加成员
        self.scroll_find("添加成员")
        from assignments.appium_practice.second_practice.page.member_invite_menu import MemberInviteMenu
        return MemberInviteMenu(self.driver)

    # 定义搜索方法
    def find_name(self, name):
        # 点击放大镜按钮
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i6n"]').click()

        # 点击搜索输入框输入内容
        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)

    def get_nameList(self, name):
        # 获取搜索结果列表
        # resultlist = self.fXpaths('//*[@resource-id="com.tencent.wework:id/bwn"]')
        sleep(2)
        resultlist = self.find(MobileBy.XPATH, f'//*[@text="{name}"]')

        # print(len(resultlist))
        return len(resultlist)

    def goto_contact_detail_page(self):
        # 点击要删除的人
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/bwn"]').click()
        return ContactDetailPage(self.driver)




