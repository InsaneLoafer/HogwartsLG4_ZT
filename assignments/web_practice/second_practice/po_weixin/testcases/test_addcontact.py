#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/8 20:41
# @Author   : ZhangTao
# @File     : test_addcontact.py

import allure
import pytest

from assignments.web_practice.second_practice.po_weixin.pages.index_pages.index_page import IndexPage


@allure.feature('测试添加成员')
class TestAddContact:

    username = 'aa'
    acctid = '1234'
    member_tel = '13411111111'

    def setup(self):
        self.index = IndexPage()

    @allure.story("测试添加成员")
    def test_addmember(self):
        # 赋值addmember
        with allure.step("点击添加成员"):
            addmember = self.index.click_add_member()
        # 进行addmember

        with allure.step("输入成员姓名、账号、电话号码"):
            addmember.add_member(self.username, self.acctid, self.member_tel)
        # 添加成员姓名到报告中
        allure.attach(self.username, '成员姓名', attachment_type=allure.attachment_type.TEXT )
        assert addmember.get_member(self.username)

if __name__ == '__main__':
    pytest.main('-v', 'test_addcontact.py')