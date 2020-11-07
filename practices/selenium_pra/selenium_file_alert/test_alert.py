#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 14:55
# @Author   : ZhangTao
# @File     : test_alert.py
from time import sleep

from selenium.webdriver import ActionChains

from practices.selenium_pra.selenium_file_alert.base import Base
"""
打开网页
操作窗口右侧页面，将元素1拖拽到元素2
这时候会有一个alert弹窗，点击弹框中的’确定‘
然后再按‘点击运行’
关闭网页
"""

class TestAlert(Base):
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')

        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

        sleep(2)
        print('点击弹窗的确认按钮')
        self.driver.switch_to.alert.accept()

        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        sleep(3)
