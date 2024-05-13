#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Max Average Subarray 1 #643

def findMaxAverage(nums: list[int], k: int) -> float:
    if k == len(nums):
        return sum(nums) / k
    window_sum = sum(nums[:k])
    max_avg = window_sum / k

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_avg = max(max_avg, window_sum / k)
    return max_avg
