#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 12:45
# @Author   : ZhangTao
# @File     : test_js.py
from time import sleep
import pytest
from practice.selenium_pra.selenium_js.base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        element = self.driver.execute_script("return document.getElementById('su')") # 利用js定位元素
        element.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000') # 滑动页面
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click() # 点击下一页
        sleep(3)
        for code in [
            'return document.title','return JSON.stringify(PerformanceTiming)'
        ]:
            print(self.driver.execute_script(code)) # 获取网页标题及性能

    def test_datetime(self):
        self.driver.get('https://www.12306.cn/index')
        date_js = "document.getElementById('train_date').removeAttribute('readonly')"
        self.driver.execute_script(date_js)
        self.driver.execute_script("document.getElementById('train_date').value='2020-10-31'")
        sleep(2)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        sleep(2)