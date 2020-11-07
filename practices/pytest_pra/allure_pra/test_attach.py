#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/5 9:59
# @Author   : ZhangTao
# @File     : test_attach.py
import allure


def test_attach_text():
    allure.attach('这是一个纯文本', attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach('<body>这是一段html body块</body>', attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file(r'D:\HogwartsLG4_ZhangTao\practice\pytest_pra\allure_pra\接口测试维度.png', attachment_type=allure.attachment_type.PNG)