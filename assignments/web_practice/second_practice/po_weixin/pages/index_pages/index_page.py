#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 19:30
# @Author   : ZhangTao
# @File     : index_page.py
from selenium.webdriver.common.by import By
from assignments.web_practice.second_practice.po_weixin.base.base_page import BasePage
from assignments.web_practice.second_practice.po_weixin.pages.index_pages.addmember_page import AddMemberPage


class IndexPage(BasePage):

    _base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    _dul_chrome = "yes"
    def click_add_member(self):
        # 点击添加成员
        self.find(By.XPATH, '//*[@class="index_service_cnt_item_title"][1]').click()
        return AddMemberPage(self._driver)
