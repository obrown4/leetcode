from ..src.two_sum_2 import twoSum
import pytest

def test1():
    numbers = [2,7,11,15]
    target = 9
    assert twoSum(numbers, target) == [1, 2]

def test2():
    n = [2,3,4]
    t = 6
    assert twoSum(n, t) == [1, 3]

def test3():
    n = [-1,0]
    t = -1
    assert twoSum(n, t) == [1, 2]
