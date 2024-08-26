class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        if not k:
            return
        
        new_start = len(nums) - k
        end = nums[:new_start].copy()
        ptr = 0
        
        for i in range(k):
            nums[i] = nums[new_start + i]
        
        for i in range(k, len(nums)):
            nums[i] = end[ptr]
            ptr += 1