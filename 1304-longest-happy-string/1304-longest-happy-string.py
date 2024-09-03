class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heappush(heap, (-a, 'a'))
        if b > 0:
            heappush(heap, (-b, 'b'))
        if c > 0:
            heappush(heap, (-c, 'c'))
        res = ""
        while heap:
            count, char = heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not heap:
                    break
                nxt_cnt, nxt_char = heappop(heap)
                res += nxt_char
                if nxt_cnt + 1 < 0:
                    heappush(heap, (nxt_cnt + 1, nxt_char))
                heappush(heap, (count, char))
            else:
                res += char
                if count + 1 < 0:
                    heappush(heap, (count + 1, char))
        return res