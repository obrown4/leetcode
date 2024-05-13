from ..src.rev_words_in_str import reverseWords
import pytest

def test_case_1():
    s = "the sky is blue"
    assert reverseWords(s) == "blue is sky the"

def test_case_2():
    s = "  hello world  "
    assert reverseWords(s) == "world hello"

def test_case_3():
    s = "a good   example"
    assert reverseWords(s) == "example good a"

def test_custom():
    s = "cambell dan city motor"
    assert reverseWords(s) == "motor city dan cambell"
