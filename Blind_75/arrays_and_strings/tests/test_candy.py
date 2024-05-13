from ..src.kids_with_candy import kidsWithCandies
import pytest

def test_case_1():
    candies = [2,3,5,1,3]
    assert kidsWithCandies(candies, 3) == [True, True, True, False, True]

def test_case_2():
    candies = [4,2,1,1,2]
    assert kidsWithCandies(candies, 1) == [True, False, False, False, False]

def test_case_3():
    candies = [12,1,12]
    assert kidsWithCandies(candies, 10) == [True, False, True]
