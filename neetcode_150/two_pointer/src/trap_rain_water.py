#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Trapping Rain Water #42
import math
def trap(height: list[int]) -> int:
    trap = 0
    l, r = 0, len(height) - 1
    max_l, max_r = height[l], height[r]

    while l < r:
        t = 0
        if height[l] <= height[r]:
            l += 1
            t = max_l - height[l]
            max_l = max(max_l, height[l])
        else:
            r -= 1
            t = max_r - height[r]
            max_r = max(max_r, height[r])
        if t > 0:
            trap += t
    return trap
