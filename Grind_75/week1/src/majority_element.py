#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Majority Element #169

from collections import defaultdict
def majorityElement(nums: list[int]) -> int:
    nums_map = defaultdict(int)
    reps = key = 0

    for num in nums:
        nums_map[num] += 1
        if nums_map[num] > reps:
           reps = nums_map[num]
           key = num
    return key
