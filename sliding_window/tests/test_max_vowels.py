from ..src.max_vowels import maxVowels
import pytest

def test_case_1():
    s = "abciiidef"
    k = 3
    assert maxVowels(s, k) == 3

def test_case_2():
    s = "aeiou"
    k = 2
    assert maxVowels(s, k) == 2

def test_case_3():
    s = "leetcode"
    k = 3
    assert maxVowels(s, k) == 2

def test_case_4():
    s = "newcastleunited"
    k = 15
    assert maxVowels(s, k) == 6

def test_case_5():
    s = "slight"
    k = 1
    assert maxVowels(s, k) == 1
