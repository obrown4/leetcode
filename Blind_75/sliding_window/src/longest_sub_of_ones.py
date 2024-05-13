#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Longest Subarray of 1's After Deleting One Element #1493

def longestSubarray(nums: list[int]) -> int:
    max_sub = l = next = num_del = 0

    for r, num in enumerate(nums):
        num_del += 1 - num

        if num_del > 0:
            num_del -= 1 - num
            l = next
            next = r + 1
            max_sub = max(max_sub, r - l)
        else:
            max_sub = max(max_sub, r - l)
    return max_sub
