#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/12 14:07
# @Author   : ZhangTao
# @File     : main.py
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from practices.appium_pra.demo.page.basepage import BasePage


class Main(BasePage):
    def goto_search(self):
        # self.find(By.ID, 'tv_search').click()
        self.steps("../page/main.yaml")

    def goto_window(self):
        # 点击编辑评论按钮，此时会触发弹窗
        self.find(By.ID, "post_status").click()
        sleep(2)
        self.find(By.ID, "tv_search").click()