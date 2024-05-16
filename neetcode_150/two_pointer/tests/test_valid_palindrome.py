from ..src.valid_palindrome import isPalindrome
import pytest

def test1():
    s = "A man, a plan, a canal: Panama"
    assert isPalindrome(s) == True

def test2():
    s = "race a car"
    assert isPalindrome(s) == False

def test3():
    s = " "
    assert isPalindrome(s) == True

def test4():
    s = "01"
    assert isPalindrome(s) == False

def test5():
    s = "010"
    assert isPalindrome(s) == True

def test6():
    s = "!@%#^$%121"
    assert isPalindrome(s) == True
