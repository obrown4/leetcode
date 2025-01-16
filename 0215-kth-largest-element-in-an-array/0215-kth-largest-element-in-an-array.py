import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        u - return kth largest element
        m - max heap to find k
        p - fill heap with negative values, and iterate and pop k times
        '''

        max_heap = []
        result = 0
        
        for n in nums:
            heapq.heappush(max_heap, -n)
        
        for i in range(0, k):
            result = -heapq.heappop(max_heap)
        return result