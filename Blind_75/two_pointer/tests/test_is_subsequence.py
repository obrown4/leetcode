from ..src.is_subsequence import isSubsequence
import pytest

def test_case_1():
    s = "abc"
    t = "ahbgdc"
    assert isSubsequence(s, t) == True

def test_case_2():
    s = "axc"
    t = "ahbgdc"
    assert isSubsequence(s, t) == False

def test_case_3():
    s = "aaa"
    t = "aheafja"
    assert isSubsequence(s, t) == True

def test_case_4():
    t = "cwhoaba"
    s = "bca"
    assert isSubsequence(s, t) == False

def test_case_5():
    s = "aec"
    t = "abcde"
    assert isSubsequence(s, t) == False
