from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # understand
        # determine # of islands 
        # need to be surrounded by 0

        # match
        # graph problem
        # bfs is likely the better choice
        # "shortest" path alg

        # plan
        # iterate through grid
        # if tile == 1 the bfs on tile
        # at each tile with 1 switch it to 0
        # increment num_islands

        rows, cols = len(grid), len(grid[0])

        def inGrid(row: int, col: int) -> bool:
            if 0 <= row < rows and 0 <= col < cols:
                return True
            return False

        def bfs(r: int, c: int) -> None:
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"

            while queue:
                row, col = queue.popleft()

                for dx, dy in directions:
                    x = dx + row
                    y = dy + col

                    if inGrid(x, y) and grid[x][y] == "1":
                        queue.append((x,y))
                        grid[x][y] = "0"
        
        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    bfs(r, c)
       
        return num_islands

