#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Move Zeroes #283
def moveZeroes(nums: list[int]) -> None:
    prev = 0
    curr = 1

    if len(nums) == 1:
        return

    while curr < len(nums):
        if nums[prev] == 0 and nums[curr] != 0:
            swapNums(prev, curr, nums)
            prev += 1
        elif nums[prev] != 0:
            prev += 1
        curr += 1

def swapNums(prev: int, curr: int, nums: list[int]) -> None:
    temp = nums[prev]
    nums[prev] = nums[curr]
    nums[curr] = temp
