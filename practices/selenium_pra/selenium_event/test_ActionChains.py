#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/5 20:49
# @Author   : ZhangTao
# @File     : test_ActionChains.py
"""
测试案例一：
打开页面：http://sahitest.com/demo/clicks.htm'
分别对‘click me’，‘dbl click me’，‘right click me’，执行点击、双击、右键操作
打印上面展示框的内容

测试案例二：
打开网页：http://sahitest.com/demo/dragDropMooTools.htm
拖拽操作

测试案例三：
打开网页：http://sahitest.com/demo/label.htm
输入文本操作
"""
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip # 忽略这个用例
    def test_case_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        ele_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        ele_double = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        ele_right = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        self.action.click(ele_click)
        self.action.context_click(ele_right) # 右键点击
        self.action.double_click(ele_double)
        sleep(3)
        self.action.perform() # 执行以上动作
        sleep(3)

    @pytest.mark.skip
    def test_move_to(self):
        self.driver.get('http://www.baidu.com')
        ele = self.driver.find_element_by_id('s-usersetting-top') # 百度首页的设置
        self.action.move_to_element(ele)
        self.action.perform()

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_ele = self.driver.find_element_by_id('dragger')
        drop1_ele = self.driver.find_element_by_xpath('//*[@class="item"][1]') # 第一个放置框
        drop2_ele = self.driver.find_element_by_xpath('//*[@class="item"][2]') # 第二个放置框
        drop3_ele = self.driver.find_element_by_xpath('//*[@class="item"][3]') # 第三个放置框
        drop4_ele = self.driver.find_element_by_xpath('//*[@class="item"][4]') # 第四个放置框

        # 方法一
        self.action.drag_and_drop(drag_ele, drop1_ele).perform() # 将第一个元素拖拽到第二个元素
        # 方法二
        self.action.click_and_hold(drag_ele).release(drop2_ele).perform() # 先按住，再释放
        # 方法三
        self.action.click_and_hold(drag_ele).move_to_element(drop3_ele).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('//input[@type="textbox"][1]')
        ele.click()
        self.action.send_keys('username').pause(1) # 输入username并暂停一秒
        self.action.send_keys(Keys.SPACE).pause(1) # 输入空格并暂停一秒
        self.action.send_keys('tom').pause(1)
        self.action.send_keys(Keys.BACK_SPACE).perform() # 删除输入的内容
        sleep(3)

# if __name__ == '__main__':
    # pytest.page(['-v', '-s', 'test_ActionChains.py'])
