#STATS
#   Runtime         Memory
#   O(klogn)            O(n)
# Top K Frequent Elements #347

from collections import defaultdict
import heapq
def kFreq(nums: list[int], k: int) -> list[int]:
    freq = defaultdict(int)
    res = []
    pq = []

    for num in nums:
        freq[num] += 1

    for key, val in freq.items():
        heapq.heappush(pq, (-val, key))

    for i in range(k):
        val = heapq.heappop(pq)
        res.append(val[1])

    return res
