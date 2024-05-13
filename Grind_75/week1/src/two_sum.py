#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Two Sum #1

def twoSum(nums: list[int], target: int) -> list[int]:
        table = {}

        for i, num in enumerate(nums):
            if target - num in table:
                return [table[target - num], i]
            table[num] = i
        return []
