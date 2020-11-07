import allure
import pytest

from assignments.pytest_practice.first_practice.test_pytest.core.calc import Calc

class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

    '''
    乘法计算测试用例
    '''
    # 整数计算正确
    @allure.feature('乘法整数计算正确测试')
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2], # 正整数计算
        [1, -1, -1], # 负整数计算
        [0, 1, 0], # 参数有零
    ])
    def test_mul1(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 浮点数计算正确
    @allure.feature('乘法浮点数计算正确测试')
    @pytest.mark.parametrize('a, b, c', [
        [0.1, 0.1, 0.01],  # 全为浮点数计算
        [1, 0.1 , 0.10] # 整数与浮点数计算
    ])
    # 判断积取两位小数是否符合预期
    def test_mul2(self, a, b, c):
        assert round(self.calc.mul(a, b), 2) == c

    # 计算错误
    @allure.feature('乘法计算错误测试')
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 1], # 正整数计算错误
        [1, -1, 1],  # 负整数计算错误
        [0, 1, 1], # 参数有零计算错误
        [0.1, 0.1, 0.1],  # 浮点数计算错误
        [0.1, 1, 1]  # 浮点数计算错误
    ])
    def test_mul3(self, a, b, c):
        assert self.calc.mul(a, b) != c

    # 输入参数类型不正确测试
    @allure.feature('乘法输入参数为非数字类型测试')
    @pytest.mark.parametrize('a, b', [
        ['a', 'b'], # 字母
        ['!', '@'], # 符号
        [' ', ' '], # 空格
        ['乘', '法'] # 汉字
    ])
    def test_mul4(self, a, b):
        # 抛出异常
        with pytest.raises(Exception):
            assert self.calc.mul(a, b)

    '''
    除法计算测试用例
    '''

    # 计算正确
    @allure.feature(('除法整数计算正确测试'))
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 0.5],  # 正整数计算
        [1, -1, -1],  # 负整数计算
        [0, 1, 0],  # 除数有零
    ])
    def test_div1(self, a, b, c):
        assert self.calc.div(a, b) == c

    @allure.feature('除法浮点数计算正确测试')
    @pytest.mark.parametrize('a, b, c', [
        [0.001, 0.1, 0.01],  # 全为浮点数计算
        [0.2, 2, 0.10] # 整数与浮点数计算
    ])
    # 判断积取两位小数是否符合预期
    def test_div2(self, a, b, c):
        assert round(self.calc.div(a, b), 2) == c

    # 计算结果为无限循环小数测试
    @allure.feature('除法的商为无限循环小数测试')
    @pytest.mark.parametrize('a, b, c', [
        [7, 3, 2.33]
    ])
    def test_div3(self, a, b, c):
        # 判断商取两位小数位是否符合预期
        assert round(self.calc.div(a, b), 2) == c

    # 计算错误
    @allure.feature('除法计算错误测试')
    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 1],  # 正整数计算错误
        [1, -1, 1],  # 负整数计算错误
        [0, 1, 1],  # 参数有零计算错误
        [0.1, 0.1, 0.1],  # 浮点数计算错误
    ])
    def test_div4(self, a, b, c):
        assert self.calc.div(a, b) != c

    # 被除数为0测试
    @allure.feature('被除数为0测试')
    @pytest.mark.parametrize('a, b', [
        [1, 0]
    ])
    def test_div5(self, a, b):
        # 抛出异常
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(a, b)

    # 输入参数类型不正确测试
    @allure.feature('除法参数类型为非数字测试')
    @pytest.mark.parametrize('a, b', [
        ['a', 'b'],  # 字母
        ['!', '@'],  # 符号
        [' ', ' '],  # 空格
        ['除', '法']  # 汉字

    ])
    def test_div6(self, a, b):
        # 抛出异常
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    # 计算顺序测试
    @allure.feature('先乘后除测试')
    @pytest.mark.parametrize('a, b', [
        [2, 1]
    ])
    def test_mul_div(self, a, b):
        assert self.calc.mul(a, b) == 2
        assert self.calc.div(a, b) == 2

    @allure.feature('先除后乘测试')
    @pytest.mark.parametrize('a, b', [
        [2, 1]
    ])
    def test_mul_div(self, a, b):
        assert self.calc.div(a, b) == 2
        assert self.calc.mul(a, b) == 2


