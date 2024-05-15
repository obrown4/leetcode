from ..src.group_anagrams import gAnagrams
import pytest

def test1():
    strs = ["eat","tea","tan","ate","nat","bat"]
    assert gAnagrams(strs) == [["bat"],["nat","tan"],["ate","eat","tea"]]

def test2():
    strs = [""]
    assert gAnagrams(strs) == [[""]]

def test3():
    s = ["a"]
    assert gAnagrams(s) == [["a"]]

def test4():
    s = ["just", "crime", "lie"]
    assert gAnagrams(s) == s
