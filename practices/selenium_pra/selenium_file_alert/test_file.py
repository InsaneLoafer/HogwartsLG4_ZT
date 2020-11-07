#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 14:38
# @Author   : ZhangTao
# @File     : test_file.py
from time import sleep

from practices.selenium_pra.selenium_file_alert.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click() # 点击照相机按钮
        self.driver.find_element_by_id('stfile').send_keys(r'D:\HogwartsLG4_ZhangTao\practice\selenium_pra\selenium_file_alert\3ntg设备.png') # 上传文件
        sleep(3)


