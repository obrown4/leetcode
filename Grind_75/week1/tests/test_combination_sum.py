from ..src.combination_sum import combinationSum
import pytest

def test_case_1():
    nums = [2,3,6,7]
    target = 7
    assert combinationSum(nums, target) == [[2,2,3],[7]]

def test_case_2():
    n = [2,3,5]
    t = 8
    assert combinationSum(n, t) == [[2,2,2,2],[2,3,3],[3,5]]

def test_case_3():
    n = [2]
    t = 1
    assert combinationSum(n, t) == []

def test_case_4():
    n = [2, 3]
    t = 10
    assert combinationSum(n, t) == [[2,2,2,2,2], [2,2,3,3]]
