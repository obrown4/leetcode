class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) == 0:
            return
        
        k = k % len(nums)
        # understand
        # rotate array k times in place
        # have the option to use O(1) space

        # match
        # two pointer potential
        # solve first with aux space

        # aux space Plan
        # keep seperate array staring at len - k
        # append len - k then append from 0 - len - k

        copy = nums.copy()
        start = len(nums) - k

        ptr = 0
        for i in range(start, len(nums)):
            nums[ptr] = copy[i]
            ptr += 1
        
        for i in range(0, start):
            nums[ptr] = copy[i]
            ptr += 1
        