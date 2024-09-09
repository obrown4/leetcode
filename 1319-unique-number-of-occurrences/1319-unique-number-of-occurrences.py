from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        occurrences = defaultdict(int)
        for n in arr:
            occurrences[n] += 1
        
        unique = set()
        for key, value in occurrences.items():
            if value in unique:
                return False
            unique.add(value)
        return True

