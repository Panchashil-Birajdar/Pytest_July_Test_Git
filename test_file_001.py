import pytest
from selenium   import webdriver
from pytest import mark


class   Test_001:

    @pytest.mark.xfail
    def test_sum_001(self):
        a = 10
        b = 20
        sum = a+b
        print('Sum of a & b is =', sum)
        if sum == 30:
            assert True
        else:
            assert False
    @pytest.mark.skip
    def test_sum_002(self):
        a = 23
        b = 34
        sum = a + b
        print("Sum of a & b =",sum)
        if  sum == 57:
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_sub_003(self):
        a = 13
        b = 7
        sub = a - b
        print("Sub of a from b =", sub)
        if sub == 6:
            assert True
        else:
            assert False































































































































































































































































