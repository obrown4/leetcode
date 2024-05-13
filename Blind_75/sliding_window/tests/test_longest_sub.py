from ..src.longest_sub_of_ones import longestSubarray
import pytest

def test_case_1():
    nums = [1,1,0,1]
    assert longestSubarray(nums) == 3

def test_case_2():
    nums = [0,1,1,1,0,1,1,0,1]
    assert longestSubarray(nums) == 5

def test_case_3():
    nums = [1,1,1]
    assert longestSubarray(nums) == 2

def test_case_4():
    nums = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]
    assert longestSubarray(nums) == 5

def test_case_5():
    nums = [1, 1, 1, 1, 0, 0, 0]
    assert longestSubarray(nums) == 4
