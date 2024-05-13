from ..src.gcd_of_strings import gcdOfStrings
import pytest


def test_case_1():
    str1 = "ABCABC"
    str2 = "ABC"
    assert gcdOfStrings(str1, str2) == "ABC"

def test_case_2():
    str1 = "ABABAB"
    str2 = "ABAB"
    assert gcdOfStrings(str1, str2) == "AB"

def test_case_3():
    str1 = "PAPS"
    str2 = "PAP"
    assert gcdOfStrings(str1, str2) == ""
