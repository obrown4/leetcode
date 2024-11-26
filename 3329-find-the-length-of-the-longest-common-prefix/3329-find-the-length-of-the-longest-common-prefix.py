class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """

        '''
        Brute Force
        compare every possible pair between arrays
        return the length of the longest prefix

        O(len(arr1) * len(arr2) * longest prefix)

        understand
        examine all possible pairs between arr1 and arr2 and return the 
        longest common prefix

        match
        two pointer with iteration

        plan
        nested for loop of arr1 and arr2
        compare until numbers != and update longest prefix
        between all pairs
        '''

        prefix_map = set()

        for num in arr1:
            num_str = str(num)

            curr_str  = ""
            for i in range(len(num_str)):
                curr_str += num_str[i]
                pre = int(curr_str)
                if pre not in prefix_map:
                    prefix_map.add(pre)
        print(prefix_map)
        longest_prefix = 0
        
        def find_prefix(num: int) -> int:
            num_str = str(num)

            curr_str = ""

            for i in range(len(num_str)):
                curr_str += num_str[i]
                curr_prefix = int(curr_str)
                if curr_prefix not in prefix_map:
                    return len(curr_str) - 1
            return len(curr_str)

        for num in arr2:
            longest_prefix = max(longest_prefix, find_prefix(num))
        return longest_prefix


        