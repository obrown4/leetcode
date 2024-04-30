from itertools import islice
import pytest
import remove_element


from remove_element import removeElement


def test_remove_element():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert removeElement(nums, 2) == 5
    assert list(islice(nums, 5)) == [0, 1, 0, 4, 3]
