#STATS
#   Runtime         Memory
#   O(n), O(n)      O(n), O(1)
# Maximum Consecutive Ones III #1004

#First Solution, Over Complicated
def longestOne(nums: list[int], k: int) -> int:
    window_size = 0
    max_window = 0
    num_flipped = 0
    zero_locs = []
    start = 0

    for i, num in enumerate(nums):
        if num == 1:
            window_size += 1
        elif num_flipped != k:
            num_flipped += 1
            zero_locs.append(i)
            window_size += 1
        else:
            max_window = max(max_window, window_size)
            zero_locs.append(i)
            zero_i = zero_locs.pop(0)
            window_size -= zero_i - start
            start = zero_i + 1
    return max(max_window, window_size)

#2nd solution a lot cleaner and simpler
def longestOnes(nums: list[int], k: int):
    left = max_window = 0

    for right, num in enumerate(nums):
        k -= 1 - num

        if k < 0:
            max_window = max(max_window, right - left)
            k += 1 - nums[left]
            left += 1
    return max(max_window, len(nums) - left)


 #nums = [1,1,1,0,0,0,1,1,1,1,0]
 #nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
