from ..src.longest_consecutive_sub import longSub
import pytest

def test1():
    nums = [100,4,200,1,3,2]
    assert longSub(nums) == 4
def test2():
    nums = [0,3,7,2,5,8,4,6,0,1]
    assert longSub(nums) == 9
def test3():
    assert longSub([]) == 0
def test4():
    assert longSub([1]) == 1
