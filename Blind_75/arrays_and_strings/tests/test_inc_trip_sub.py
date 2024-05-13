from ..src.increasing_triplet_sub import increasingTriplet
import pytest

def test_case_1():
    nums = [1,2,3,4,5]
    assert increasingTriplet(nums) == True

def test_case_2():
   nums = [5,4,3,2,1]
   assert increasingTriplet(nums) == False

def test_case_3():
    nums = [2,1,5,0,4,6]
    assert increasingTriplet(nums) == True

def test_case_4():
    nums = [5,3,2,3,4]
    assert increasingTriplet(nums) == True

def test_case_5():
    nums = [20,100,10,12,5,13]
    assert increasingTriplet(nums) == True
