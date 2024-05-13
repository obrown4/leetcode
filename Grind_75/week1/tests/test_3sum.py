from ..src.three_sum import threeSum
import pytest

def test_case_1():
    nums = [-1,0,1,2,-1,-4]
    assert threeSum(nums) == [[-1,-1,2],[-1,0,1]]

def test_case_2():
    nums = [0,1,1]
    assert threeSum(nums) == []

def test_case_3():
    nums = [0,0,0]
    assert threeSum(nums) == [[0,0,0]]

def test_case_4():
    nums = [-3, -3, 4, 1, 2]
    assert threeSum(nums) == [[-3, 1, 2]]
