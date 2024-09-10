from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_map = defaultdict(int)
        col_map = defaultdict(list)

        for r, row in enumerate(grid):
            for c in range(len(grid)):
                col_map[c].append(grid[r][c])
            row_map[tuple(row)] += 1
        
        res = 0
        for key, value in col_map.items():
            if tuple(value) in row_map:
                res += row_map[tuple(value)]
        return res
        
