from ..src.move_zeroes import moveZeroes
import pytest

def test_case_1():
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0]

def test_case_2():
    nums = [0]
    moveZeroes(nums)
    assert nums == [0]

def test_case_3():
    nums = [0, 1, 0, 2, 0, 4, 0, 5]
    moveZeroes(nums)
    assert nums == [1, 2, 4, 5, 0, 0, 0, 0]
