from ..src.string_compression import    compress
import pytest

def test_case_1():
    chars = ["a","a","b","b","c","c","c"]
    assert compress(chars) == 6

def test_case_2():
    chars = ["a"]
    assert compress(chars) == 1

def test_case_3():
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    assert compress(chars) == 4

def test_case_4():
    chars = ["b","b","b","b","b","b","b","b","b","b","b","b", "a"]
    assert compress(chars) == 4
