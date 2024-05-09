from ..src.max_avg_sub_array import findMaxAverage
import pytest

def test_case_1():
    nums = [1,12,-5,-6,50,3]
    k = 4
    assert findMaxAverage(nums, k) == 12.75

def test_case_2():
    nums = [5]
    k = 1
    assert findMaxAverage(nums, k) == 5.0

def test_case_3():
    nums = [0,1,1,3,3]
    k = 4
    assert findMaxAverage(nums, k) == 2.00
