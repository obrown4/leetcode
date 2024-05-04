#STATS
#   Runtime         Memory
#   O(n) beats 45%  O(n) beats 30%
# Product of Array except Self #238

import math
def productExceptSelf(nums: list[int]) -> list[int]:

    res = [0] * len(nums)
    z_count = 0
    total = 1

    for num in nums:
        if num == 0:
            z_count += 1
        else:
            total *= num

    if z_count > 1:
        return res

    for i, num in enumerate(nums):
        if num == 0:
            res[i] = total
        elif z_count == 0:
            res[i] = total // num
    return res
