from ..src.flower_bed import canPlaceFlowers
import pytest

def test_case_1():
    flowerbed = [1,0,0,0,1]
    assert canPlaceFlowers(flowerbed, 1) == True

def test_case_2():
    flowerbed = [1,0,0,0,1]
    assert canPlaceFlowers(flowerbed, 2) == False

def test_case_3():
    flowerbed = [0, 1, 0, 0, 1, 0, 0]
    assert canPlaceFlowers(flowerbed, 1) == True

def test_case_4():
    flowerbed = [1,0,0,0,0,1]
    assert canPlaceFlowers(flowerbed, 2) == False

def test_case_5():
    flowerbed = [0, 0, 1, 0, 1]
    assert canPlaceFlowers(flowerbed, 1) == True

def test_case_6():
    flowerbed = [0, 1, 0]
    assert canPlaceFlowers(flowerbed, 1) == False
