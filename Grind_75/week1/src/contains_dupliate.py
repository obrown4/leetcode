#STATS
#   Runtime         Memory
#   O(n)            O(n)
# Contains Duplicate #217

def containsDuplicate(nums: list[int]) -> bool:
    num_set = set()

    for num in nums:
        if num not in num_set:
            num_set.add(num)
        else:
            return True
    return False
