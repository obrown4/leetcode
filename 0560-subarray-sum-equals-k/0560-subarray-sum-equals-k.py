from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # understand
        # return num of sub arrays that sum to k

        # match 
        # prefix sum
        # hash map

        # plan
        # iterate over nums
        # keep track of current sum
        # if curr == k += count
        # look in map for curr - k and += to count
        # means that by removing that node we can get to k n times
        # return count

        seen = defaultdict(int)
        curr_sum = count = 0

        for n in nums:
            curr_sum += n
            if curr_sum == k:
                count += 1
            
            count += seen[curr_sum - k]
            seen[curr_sum] += 1
        return count
            
        