#remove element
def removeElement( nums: list[int], val: int) -> int:
    #start from end of nums and hold ptr on first value != val
    #once we find a value that equals val swithc places and update ptrs

    prev = len(nums) - 2
    end = len(nums) - 1
    k = 0
    if nums[end] != val:
        k += 1

    while prev >= 0:
        if nums[prev] != val:
            k += 1
        if nums[end] != val and nums[prev] == val:
            nums[prev] = nums[end]
            end -= 1
        elif nums[end] == val:
            end -= 1
        prev -= 1
    return k
