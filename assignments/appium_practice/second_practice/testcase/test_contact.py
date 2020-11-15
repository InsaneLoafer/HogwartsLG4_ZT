#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/15 20:16
# @Author   : ZhangTao
# @File     : test_contact.py

"""
测试添加联系人
"""
import pytest
from assignments.appium_practice.second_practice.page.app import App

class TestWX:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name, gender, phonenum',[
        ['bb12', '男', '13311221122'],
        ['bb13', '女', '13322112211']
    ])
    def test_add_contact(self, name, gender, phonenum):
        result = self.main.goto_contaclist().goto_member_invite_menu().\
            add_member_manul().add_member(name, gender, phonenum).get_toast_text()

        assert result == "添加成功"

    @pytest.mark.parametrize('name', ['bb12', 'bb13'])
    def test_del_contact(self, name):
        contact = self.main.goto_contaclist()
        # 点击搜索进行搜索
        contact.find_name(name)
        # 获取列表
        origin_list = contact.get_nameList(name)
        # 进行删除
        contact.goto_contact_detail_page().goto_contact_setting().goto_contact_edit().del_contact()
        # 再次获取列表
        final_list = contact.get_nameList(name)

        assert origin_list - final_list == 1




