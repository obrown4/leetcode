#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Product of Array Except Self #238

def productExceptSelf(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    post = 1
    pre = 1

    for i in range(len(nums) - 1, -1, -1):
        temp = nums[i]
        res[i] = post
        post *= nums[i]

    for i, num in enumerate(nums):
        res[i] *= pre
        pre *= num
    return res
