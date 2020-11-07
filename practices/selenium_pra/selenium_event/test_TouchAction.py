#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/5 22:01
# @Author   : ZhangTao
# @File     : test_TouchAction.py
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False) # 将w3c格式屏蔽掉
        self.driver = webdriver.Chrome(options=option)
        self.action = TouchActions(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbotton(self):
        """
        打开Chrome
        打开URL：http://www.baidu.com
        向搜索框输入“selenium测试”
        通过TouchAction点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        :return:
        """
        self.driver.get('http://www.baidu.com')
        ele_input = self.driver.find_element_by_id('kw')
        ele_search = self.driver.find_element_by_id('su')
        ele_input.send_keys("selenium测试")
        self.action.tap(ele_search) # 触摸搜索按钮
        self.action.scroll_from_element(ele_input, 0, 10000).perform() # 滚动页面，添加坐标偏移量


