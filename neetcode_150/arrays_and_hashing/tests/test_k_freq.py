from ..src.k_freq_elements import kFreq
import pytest

def test1():
    nums = [1,1,1,2,2,3]
    k = 2
    assert kFreq(nums, k) == [1, 2]

def test2():
    nums = [1]
    k = 1
    assert kFreq(nums, k) == [1]

def test3():
    nums = [1,2,2,2,2,3]
    k = 1
    assert kFreq(nums, k) == [2]

def test4():
    nums = [1, 2, 2,1, 2, 3]
    k = 3
    assert kFreq(nums, k) == [2, 1, 3]
