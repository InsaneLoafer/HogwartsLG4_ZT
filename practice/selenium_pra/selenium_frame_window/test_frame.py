#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/6 10:54
# @Author   : ZhangTao
# @File     : test_frame.py
from time import sleep
from selenium.webdriver import ActionChains
from practice.selenium_pra.selenium_frame_window.base import Base

class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult') # 切换frame
        drop = self.driver.find_element_by_id('droppable')
        drag = self.driver.find_element_by_id('draggable')
        print(drag.text, drop.text)
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop)
        self.driver.switch_to.parent_frame() # 切换回父节点
        # self.driver.switch_to.default_content() # 切换回默认frame(与切换回父节点一致）
        print(self.driver.find_element_by_id('submitBTN').text)
        sleep(3)


