from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def inGrid(row: int, col: int) -> bool:
            if 0 <= row < rows and 0 <= col < cols:
                return True
            return False
        
        def bfs(row: int, col: int) -> int:
            queue = deque()
            queue.append((row, col))
            grid[row][col] = 0
            area = 1

            while queue:
                r, c = queue.popleft()
                for dx, dy in directions:
                    x = r + dx
                    y = c + dy

                    if inGrid(x, y) and grid[x][y] == 1:
                        area += 1
                        grid[x][y] = 0
                        queue.append((x,y))
            return area
        
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        return max_area
