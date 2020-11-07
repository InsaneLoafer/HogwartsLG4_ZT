#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time     : 2020/11/2 20:28
# @Author   : ZhangTao
# @File     : test_a.py
import pytest

def func(x):
    return x+1

@pytest.mark.parametrize('a, b', [
    (1, 2),
    ((10, 20))
])
def test_answer(a, b):
    assert func(a) == b

# def test_answer1():
    # assert func(3) == 5

@pytest.fixture()
def login():
    print('登陆操作')
    username = 'michael'
    return username

class TestDemo:
    def test_a(self, login):
        print(f'a  username = {login}')

    def test_b(self):
        print('b')

    def test_c(self, login):
        print(f'c  login = {login}')

if __name__ == '__main__':
    pytest.main(["test_a.py::TestDemo",'-v']) # -v打印详细日志，模仿命令行运行
