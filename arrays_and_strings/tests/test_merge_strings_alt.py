from ..src.merge_strings_alt import mergeAlternately
import pytest

def test_merge_eq_size():
    word1 = "abc"
    word2 = "pqr"
    assert mergeAlternately(word1, word2) == "apbqcr"
def test_merge_uneq_size():
    word1 = "trews"
    word2 = "b"
    assert mergeAlternately(word1, word2) == "tbrews"
