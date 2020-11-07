#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/4 9:28
# @Author   : ZhangTao
# @File     : test_weixin.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import *
import random
import shelve
import os
import allure

"""
复用浏览器：
将chrome添加到环境变量，cmd里面执行：
chrome  --remote-debugging-port=9222
"""
def generate_info():
    # 随机生成五位成员id
    id = random.randint(10000, 99999)

    # 生成成员名称
    username = f'michael{id}'

    # 随机生成电话号码
    # 第二位数字
    second = random.choice([3, 5, 6, 7, 8, 9])
    #其余非首位数字
    other = random.randint(100000000, 999999999)
    phonenumber = f'1{second}{other}'

    return username, id, phonenumber

@allure.feature('微信添加联系人测试')
class TestWeixin:

    def setup(self):
        option = Options()
        option.debugger_address ="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.url = "https://work.weixin.qq.com/wework_admin/frame#index"
        self.driver.implicitly_wait(5) # 隐式等待5秒
        # self.driver.maximize_window() # 窗口最大化

    def teardown(self):
        self.driver.quit()
        pass

    def save_cookies(self):
        self.driver.get(self.url)
        cookies = self.driver.get_cookies() # 获取cookies
        print(cookies)
        # 剔除cookie有效期时间戳
        db = shelve.open('cookies') # 使用shelve数据库，以键值对存储
        cookies = db['cookie']
        db.close()
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

    def add_contact(self, username, id, phone_number):
        self.driver.refresh() # 刷新页面
        self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click() # 点击添加成员
        self.driver.find_element_by_id('username').send_keys(username) # 输入成员姓名
        self.driver.find_element_by_id('memberAdd_acctid').send_keys(id) # 输入成员账号
        self.driver.find_element_by_id('memberAdd_phone').send_keys(phone_number) # 输入成员电话号码
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.js_btn_save").click()  # 点击保存
        mlist = self.driver.find_elements(By.XPATH, '//*[@id="member_list"]/tr//span')  # 获取成员列表
        memberlist = []
        for m in mlist:
            member = m.text
            memberlist.append(member)
        return memberlist

    @allure.story('添加联系人')
    def test_add_contact(self):
        username, id, phonenumber = generate_info()

        # 判断是否生成cookies.dat文件
        if os.path.exists('cookies.dat'):
            # 调用add_contact函数
            memberlist = self.add_contact(username, id, phonenumber)
            # 判断新增成员是否在成员列表中
            assert username in memberlist

        else:
            # 调用save_cookies函数
            self.save_cookies()
            # 调用add_contact函数
            memberlist = self.add_contact(username, id, phonenumber)
            # 判断新增成员是否在成员列表中
            assert username in memberlist

if __name__ == '__main__':
    pytest.main(['test_weixin.py', '-v'])






