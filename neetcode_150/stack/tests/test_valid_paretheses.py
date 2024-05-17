from ..src.valid_parentheses import isValid
import pytest

def test1():
    s = "()"
    assert isValid(s) == True

def test2():
    s = "()[]{}"
    assert isValid(s) == True

def test3():
    s = "(]"
    assert isValid(s) == False

def test4():
    s = "([])"
    assert isValid(s) == True

def test5():
    s = ")("
    assert isValid(s) == False

def test6():
    s = "("
    assert isValid(s) == False
