from ..src.max_pairs import maxOperations
import pytest

def test_case_1():
    nums = [1,2,3,4]
    k = 5
    assert maxOperations(nums, k) == 2

def test_case_2():
    nums = [3,1,3,4,3]
    k = 6
    assert maxOperations(nums, k) == 1
