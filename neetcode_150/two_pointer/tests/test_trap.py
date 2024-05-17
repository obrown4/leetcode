from ..src.trap_rain_water import trap
import pytest

def test1():
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert trap(height) == 6

def test2():
    height = [4,2,0,3,2,5]
    assert trap(height) == 9

def test3():
    h = [2,1,0,1,0,1]
    assert trap(h) == 2

def test4():
    h = [3, 2, 1, 0, 0, 1, 2]
    assert trap(h) == 6

def test5():
    h = [3, 2, 1, 0, 0, 1, 1]
    assert trap(h) == 2
