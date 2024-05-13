from ..src.reverse_vowels import reverseVowels
import pytest

def test_case_1():
    s = "hello"
    assert reverseVowels(s) == "holle"

def test_case_2():
    s = "leetcode"
    assert reverseVowels(s) == "leotcede"

def test_case3():
    s = "eat"
    assert reverseVowels(s) == "aet"
