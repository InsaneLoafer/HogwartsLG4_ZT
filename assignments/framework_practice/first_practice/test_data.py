#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/19 9:36
# @Author   : ZhangTao
# @File     : test_data.py
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 定义读取文件方法
def load_data(path):
    with open (path, encoding="utf-8") as f:
        return yaml.load(f)

class TestData:
    # 测试搜索并跳转到下一页
    yaml_data = load_data("data.yaml")
    @pytest.mark.parametrize('data', yaml_data["data"])
    def test_search_and_scroll(self, data):
        # 对测试步骤进行数据驱动
        steps = self.yaml_data["steps"]
        for step in steps:
            # 如果webdriver在测试步骤中，则进行浏览器判断
            if 'webdriver' in step:
                # 默认给浏览器赋值为chrome
                browser = str(step.get('webdriver').get('browser', 'chrome')).lower()
                if browser == 'chrome':
                    driver = webdriver.Chrome()
                    driver.maximize_window()
                    driver.implicitly_wait(5)
                elif browser == 'firefox':
                    driver = webdriver.Firefox()
                    driver.maximize_window()
                    driver.implicitly_wait(5)
                else:
                    print('输入的浏览器名称不正确')

            # 如果get在测试步骤中，就进行访问url
            if 'get' in step:
                driver.get(step.get('get'))

            # 定义find_element数据驱动
            if 'find_element' in step:
                # 如果是列表
                if isinstance(step.get("find_element"), list):
                    by = step.get("find_element")[0]
                    locator = step.get("find_element")[1]
                    element = driver.find_element(by, locator)
                    operations = step.get("find_element")[2]
                    for operation in operations:
                        if 'click' in operation:
                            element.click()
                        if 'send_keys' in operation:
                            value = str(operation.get('send_keys'))
                            # 判断value是否是变量 ${data}
                            value = value.replace('${data}', data)
                            element.send_keys(value)

                # 如果是字典
                elif isinstance(step.get("find_element"), dict):
                    by = step.get("find_element")['by']
                    locator = step.get("find_element")['locator']
                    element = driver.find_element(by, locator)
                    operations = step.get("find_element")['operation']
                    for operation in operations:
                        if 'click' in operation:
                            element.click()
                        if 'send_keys' in operation:
                            value = str(operation.get('send_keys'))
                            # 判断value是否是变量 ${data}
                            value = value.replace('${data}', data)
                            element.send_keys(value)

            # 定义滑动点击操作
            if 'scroll_find' in step:
                # 滑动页面
                driver.execute_script('document.documentElement.scrollTop=10000')
                by = step.get('scroll_find')['by']
                locator = step.get('scroll_find')['locator']
                operations = step.get("find_element")['operation']
                # 显示等待目标元素出现
                WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(locator))
                dst_element = driver.find_element(by, locator)
                for operation in operations:
                    if 'click' in operation:
                        dst_element.click()



