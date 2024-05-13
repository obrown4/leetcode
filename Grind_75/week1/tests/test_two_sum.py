from ..src.two_sum import twoSum
import pytest

def test_case_1():
    nums = [2,7,11,15]
    target = 9
    assert twoSum(nums, target) == [0,1]

def test_case_2():
    nums = [3,2,4]
    target = 6
    assert twoSum(nums, target) == [1,2]

def test_case_3():
    nums = [3,3]
    target = 6
    assert twoSum(nums, target) == [0,1]
