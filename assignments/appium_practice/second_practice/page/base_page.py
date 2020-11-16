#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 16:52
# @Author   : ZhangTao
# @File     : base_page.py
import logging
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    # 定义日志格式
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='../log/myapp.log',
                        filemode='w')

    # 初始化driver
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 定义find方法
    def find(self, by, locator):
        logging.info("find:")
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        logging.info("finds:")
        logging.info(by)
        logging.info(locator)
        return self.driver.find_elements(by, locator)

    # 定义滚动查找操作
    def scroll_find(self, text):
        logging.info("scroll_find:")
        logging.info(text)
        self.find(MobileBy.ANDROID_UIAUTOMATOR,
                  'new UiScrollable(new UiSelector()'
                  '.scrollable(true).instance(0))'
                  '.scrollIntoView(new UiSelector()'
                  f'.text("{text}").instance(0));').click()

    # 定义显示等待方法
    def webdriver_wait(self, time, locator):
        logging.info("WebDriverWait:")
        logging.info(f"time：{time}")
        logging.info(locator)
        # 直到某个元素能够点击
        WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))

    # 定义获取toast文本方法
    def get_toast_text(self):
        logging.info("get toast:")
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result

