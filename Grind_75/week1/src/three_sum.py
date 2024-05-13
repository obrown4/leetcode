#STATS
#   Runtime         Memory
#   O(n^2)          O(n)
# 3Sum #15

from collections import defaultdict
def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []

    for i, num1 in enumerate(nums):
        begin = i + 1
        end = len(nums) - 1
        if i > 0 and nums[i-1] == num1:
            continue
        while begin < end:
            s = num1 + nums[begin] + nums[end]
            if s < 0:
                begin += 1
            elif s > 0:
                end -= 1
            else:
                res.append([num1, nums[begin], nums[end]])
                begin += 1
                while nums[begin] == nums[begin - 1] and begin < end:
                    begin += 1
    return res
