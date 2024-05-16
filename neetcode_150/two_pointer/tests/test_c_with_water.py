from ..src.contianer_w_most_water import maxArea
import pytest

def test_case_1():
    height = [1,8,6,2,5,4,8,3,7]
    assert maxArea(height) == 49

def test_case_2():
    h = [1, 1]
    assert maxArea(h) == 1

def test_case_3():
    h = [1, 10, 2, 1, 1, 1, 0, 0, 1]
    assert maxArea(h) == 8

def test_case_4():
    h = [5, 2, 1, 2, 1, 4, 3, 5, 100, 100]
    assert maxArea(h) == 100

def test_case_5():
    h = [1, 8, 2, 3, 4, 8, 10, 2, 6]
    assert maxArea(h) == 42
