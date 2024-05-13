from itertools import islice
from ..src.remove_element import removeElement
import pytest

def test_remove_element():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert removeElement(nums, 2) == 5
    assert list(islice(nums, 5)) == [0, 1, 0, 4, 3]
