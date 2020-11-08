#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 19:45
# @Author   : ZhangTao
# @File     : addmember_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from assignments.web_practice.second_practice.po_weixin.base.base_page import BasePage

class AddMemberPage(BasePage):

    def add_member(self, username, memberAdd_acctid, memberAdd_phone):
        # 输入成员姓名
        self.find(By.ID, 'username').send_keys(username)
        # 输入账号
        self.find(By.ID, 'memberAdd_acctid').send_keys(memberAdd_acctid)
        # 输入电话
        self.find(By.ID, 'memberAdd_phone').send_keys(memberAdd_phone)
        # 点击保存
        self.find(By.LINK_TEXT, '保存').click()

    def get_member(self, member_name):
        # 显示等待
        locator =(By.CLASS_NAME, 'ww_checkbox')
        self.wait_for_click(locator)
        # 定义所有成员姓名列表
        names_total = []
        while True:
            # 获取成员姓名列表
            members = self.finds(By.XPATH, '//*[@id="member_list"]/tr/td[2]')
            names = [member.get_attribute("title") for member in members]
            # 如果所查找成员在列表里，就返回True
            if member_name in names:
                return True
            names_total.extend(names)

            # 如果名单有分页
            if expected_conditions.invisibility_of_element((By.CSS_SELECTOR, ".ww_pageNav_info_text")):
                page:str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
                # 通过反斜杠分割
                num, total = page.split('/')
            # 判断当前页码是否与总页码相等
                if num != total:
                    # 如果不相等就继续翻页
                    self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()
                else:
                    return False
        return names_total



