#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Max Number of K-Sum Pairs #1679

def maxOperations(nums: list[int], k: int) -> int:
    nums.sort()
    num_ops, begin, end = 0, 0, len(nums) - 1

    while begin < end:
        target = nums[begin] + nums[end]
        if target == k:
            num_ops += 1
            begin += 1
            end -= 1
        elif target < k:
            begin += 1
        else:
            end -= 1
    return num_ops
