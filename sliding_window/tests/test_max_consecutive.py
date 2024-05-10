from ..src.max_consecutive_ones import longestOnes
import pytest

def test_case_1():
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    assert longestOnes(nums, k) == 6

def test_case_2():
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    k = 3
    assert longestOnes(nums, k) == 10

def test_case_3():
    nums = [0, 0, 0, 1, 1, 1, 1, 0]
    k = 1
    assert longestOnes(nums, k) == 5

def test_case_4():
    nums = [0, 0, 0, 0, 0]
    k = 5
    assert longestOnes(nums, k) == 5

def test_case_5():
    nums = [0, 1, 0, 1, 0, 1, 0, 1, 1, 0]
    k = 3
    assert longestOnes(nums, k) == 8
