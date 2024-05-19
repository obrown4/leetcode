from ..src.generate_parentheses import genP
import pytest

def test1():
    n = 3
    assert genP(n) == ["((()))","(()())","(())()","()(())","()()()"]

def test2():
    assert genP(1) == ["()"]
