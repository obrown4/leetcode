class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        res1 = []
        res2 = []

        for n in set1:
            if n not in set2:
                res1.append(n)

        for n in set2:
            if n not in set1:
                res2.append(n)

        return [res1, res2]