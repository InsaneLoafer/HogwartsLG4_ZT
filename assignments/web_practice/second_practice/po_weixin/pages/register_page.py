#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 19:17
# @Author   : ZhangTao
# @File     : register_page.py
from selenium.webdriver.common.by import By
from assignments.web_practice.second_practice.po_weixin.base.base_page import BasePage


class RegisterPage(BasePage):
    def register(self, company_name, manager_name, register_tel):
        # 输入企业名称
        self.find(By.ID, 'corp_name').send_keys(company_name)
        # 输入管理员姓名
        self.find(By.ID, 'manager_name').send_keys(manager_name)
        # 输入管理利用手机号
        self.find(By.ID, 'register_tel').send_keys(register_tel)
        # 勾选同意协议
        self.find(By.ID, 'iagree').click()
        # 点击注册按钮
        # self.find(By.ID, 'submit_btn').click()