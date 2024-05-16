#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Container with The Most Water

def maxArea(height: list[int]) -> int:
    l , r = 0, len(height) - 1
    max_area = 0

    while l < r:
        area = min(height[l], height[r]) * (r - l)

        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l += 1
            r -= 1
        max_area = max(area, max_area)
    return max_area
