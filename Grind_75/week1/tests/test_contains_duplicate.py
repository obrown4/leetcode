from ..src.contains_dupliate import containsDuplicate
import pytest

def test_case_1():
    nums = [1,2,3,1]
    assert containsDuplicate(nums) == True

def test_case_2():
    nums = [1, 2, 3, 4, 5]
    assert containsDuplicate(nums) == False

def test_case_3():
    nums = [1]
    assert containsDuplicate(nums) == False

def test_case_4():
    nums = [1,1,1,3,3,4,3,2,4,2]
    assert containsDuplicate(nums) == True
