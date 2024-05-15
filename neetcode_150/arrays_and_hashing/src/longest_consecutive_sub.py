#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Longest Consecutive Subsequence #128

def longSub(nums: list[int]) -> int:
    nums_set = set(nums)
    max_seq = 0

    for num in nums:
        curr_seq = 0
        if num - 1 not in nums_set:
            while num + curr_seq in nums_set:
                curr_seq += 1
        max_seq = max(max_seq, curr_seq)
    return max_seq
