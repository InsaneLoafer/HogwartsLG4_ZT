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

    @pytest.mark.skip
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

    def test_search1(self):
        """
        1、打开雪球  应用首页
        2、定位首页的搜索框
        3、判断搜索框是否可用，并查看搜索框name值
        4、打印搜索框这个元素的左上角坐标和它的宽高
        5、向搜索框输入‘alibaba‘
        6、判断’阿里巴巴‘是否可见
        7、如果可见，则打印’搜索成功‘；不可见则打印’搜索失败‘
        :return:
        """
        search_ele = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        if search_ele.is_enabled():
            print(search_ele.text)
            print(search_ele.location)
            print(search_ele.size)

            search_ele.click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            ali_element = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]')
            if ali_element.is_displayed() == 'true':
                print('搜索成功')
            else:
                print('搜索失败')


if __name__ == '__main__':
    pytest.main()

