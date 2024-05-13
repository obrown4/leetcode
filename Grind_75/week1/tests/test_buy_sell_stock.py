from ..src.best_time_to_buy_stock import maxProfit
import pytest

def test_case_1():
    prices = [7,1,5,3,6,4]
    assert maxProfit(prices) == 5

def test_case_2():
    prices = [7,6,4,3,1]
    assert maxProfit(prices) == 0

def test_case_3():
    prices = [10, 30, 2, 3, 5]
    assert maxProfit(prices) == 20

def test_case_4():
    assert maxProfit([1]) == 0
