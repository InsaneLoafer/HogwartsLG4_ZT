#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 10:00
# @Author   : ZhangTao
# @File     : test_window.py
from time import sleep

from practices.selenium_pra.selenium_frame_window.base import Base

class TestWindow(Base):
    def test_window(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_css_selector('#u1>span+a').click() # 点击登录
        self.driver.find_element_by_link_text('立即注册').click() # 点击注册
        cwindow = self.driver.current_window_handle # 获取当前窗口句柄
        windows = self.driver.window_handles # 获取所用窗口句柄
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username') # 输入用户名
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('13313313313') # 输入手机号
        self.driver.find_element_by_id('TANGRAM__PSP_4__password').send_keys('jinhua911love!') # 输入密码
        sleep(3)

        self.driver.switch_to_window(cwindow) # 切换到之前的窗口
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click() # 点击用户名登录
        sleep(2)
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('username') # 输入用户名
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('password')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click() # 点击登录
        sleep(3)