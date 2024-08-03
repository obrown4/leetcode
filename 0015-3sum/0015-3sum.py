class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # u
        # return trips that sum to 0

        # match
        # two pointer

        # plan
        # sort nums
        # start base pointer at 0 then have b + 1 and end ptr
        # move l and r accordingly 
        # if b ptr == b - 1 ptr then continue
        
        nums.sort()
        trips = []
        for base in range(len(nums)):
            l, r = base + 1, len(nums) - 1

            if base > 0 and nums[base - 1] == nums[base]:
                continue
            
            while l < r:
                curr = nums[base] + nums[l] + nums[r]

                if curr < 0:
                    l += 1
                elif curr > 0:
                    r -= 1
                else:
                    trips.append([nums[base], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return trips