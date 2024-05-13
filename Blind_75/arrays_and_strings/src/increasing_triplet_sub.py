#STATS
#   Runtime         Memory
#   O(n)            O(1)
# Inreasing Triplet Subsequence #334

def increasingTriplet(nums: list[int]) -> bool:
    prev = next = float('inf')

    for num in nums:
        if num <= prev:
            prev = num
        elif num <= next:
            next = num
        else:
            return True
    return False
