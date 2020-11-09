#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/9 22:07
# @Author   : ZhangTao
# @File     : test_dwpytest.py
import pytest
from appium import webdriver
class TestDW():
    def setup(self):
        desire_caps = {
            "platformName": "Android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".common.MainActivity",
            "noReset": False,
            "skipDeviceInitialization": True,
            # "dontStopAppOnReset": True,
            "unicodeKeyBoard": True, # 设置后可输入中文
            "resetKeyBoard": True # 重置键盘
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print('搜索测试用例')
        """
        1、打开雪球app
        2、点击搜索框
        3、输入‘阿里巴巴’
        4、在搜索结果中选择‘阿里巴巴’，并点击
        5、获取这只阿里巴巴的股价，并判断这只股票的价格>200
        """
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        current_price = self.driver.find_element_by_id('com.xueqiu.android:id/current_price').text
        assert current_price > 200
if __name__ == '__main__':
    pytest.main()

