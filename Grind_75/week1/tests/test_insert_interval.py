from ..src.insert_interval import insert
import pytest

def test_case_1():
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    assert insert(intervals, newInterval) == [[1,2], [3,10],[12,16]]

def test_case_2():
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    assert insert(intervals, newInterval) == [[1,5], [6,9]]

def test_case_3():
    i = [[0,5], [6,10], [15,20]]
    new_i = [0, 25]
    assert insert(i, new_i) == [[0,25]]

def test_case_4():
    i = []
    new_i = [1,3]
    assert insert(i, new_i) == [[1,3]]

def test_case_5():
    i = [[0, 3], [5, 8], [10,10]]
    new_i = [6,7]
    assert insert(i, new_i) == i
