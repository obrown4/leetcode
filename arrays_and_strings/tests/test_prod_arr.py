from ..src.product_of_arr_but_self import productExceptSelf
import pytest

def test_case_1():
    nums = [1,2,3,4]
    assert productExceptSelf(nums) == [24, 12, 8, 6]

def test_case_2():
    nums = [-1,1,0,-3,3]
    assert productExceptSelf(nums) == [0, 0, 9, 0, 0]

def test_custom():
    nums = [10, 2, 3, 0, 5, 0]
    assert productExceptSelf(nums) == [0, 0, 0, 0, 0, 0]
