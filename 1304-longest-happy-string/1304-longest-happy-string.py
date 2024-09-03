import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # happy = only a, b, c

        # plan
        # first greatest letter count
        # at each letter if possible place 2
        # iterate in range of the sum of the letters
        # at each position append greatest letter and then smaller letter 
        # if there are no aux letters left break the loop return the string

        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        
        happy_string = []

        while heap:
            val, char = heapq.heappop(heap)
            if len(happy_string) >= 2 and happy_string[-1] == happy_string[-2] == char:
                if not heap:
                    break
                val_pad, char_pad = heapq.heappop(heap)
                
                happy_string.append(char_pad)

                if val_pad + 1 < 0:
                    heapq.heappush(heap, (val_pad + 1, char_pad))
                heapq.heappush(heap, (val, char))
            else:
                happy_string.append(char)
                if val + 1 < 0:
                    heapq.heappush(heap, (val + 1, char))
        return "".join(happy_string)



 