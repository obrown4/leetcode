#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Two Sum II - Input Array is Sorted #167

def twoSum(number: list[int], target: int) -> list[int]:
    l, r = 0, len(number) - 1

    while l < r:
        sum = number[l] + number[r]
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return [l + 1, r + 1]
    return []
