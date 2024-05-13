from ..src.majority_element import majorityElement
import pytest

def test_case_1():
    nums = [3,2,3]
    assert majorityElement(nums) == 3

def test_case_2():
    nums = [2,2,1,1,1,2,2]
    assert majorityElement(nums) == 2

def test_case_3():
    nums = [1]
    assert majorityElement(nums) == 1

def test_case_4():
    nums = [2,1, 3, 4, 5, 3, 2, 1, 3, 2, 2, 7]
    assert majorityElement(nums) == 2
