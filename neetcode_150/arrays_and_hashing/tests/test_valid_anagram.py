from ..src.valid_anagram import isAnagram
import pytest

def test_case_1():
    s = "anagram"
    t = "nagaram"
    assert isAnagram(s, t) == True

def test_case_2():
    s = "rat"
    t = "car"
    assert isAnagram(s, t) == False
