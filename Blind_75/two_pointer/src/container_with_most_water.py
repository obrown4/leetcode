#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Container with the Most Water #11
def maxArea(height: list[int]) -> int:
    begin = 0
    end = len(height) - 1
    max = -1

    while begin != end and end - begin > 0:
        curr_area = min(height[begin], height[end]) * (end - begin)
        if curr_area > max:
            max = curr_area
        if height[begin] < height[end]:
            begin += 1
        else:
            end -= 1
    return max
# 1, 8, 6, 2, 5, 4, 8, 3, 7
# [1, 10, 2, 1, 1, 1, 0, 0, 1]
