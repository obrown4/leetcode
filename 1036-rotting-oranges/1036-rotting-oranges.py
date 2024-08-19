from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # understamd
        # how many cycles till rot spreads 

        # match
        # graph problem
        # bfs 

        # plan
        # init queue with rotten tiles
        # keep count of number of fresh oranges
        # bfs on queue and add each surrounding element that isn't rotten
        # mark as rotten in grid
        # decrement orange count and increment cycles

        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        num_oranges = 0
        cycles = 0

        queue = deque()
        def inGrid(r: int, c: int) -> bool:
            if 0 <= r < rows and 0 <= c < cols:
                return True
            return False
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    num_oranges += 1
        
        if not num_oranges:
            return 0
        
        # bfs
        while queue:
            curr = len(queue)
            cycles += 1
            
            for i in range(curr):
                row, col = queue.popleft()
                for dx, dy in directions:
                    x = row + dx
                    y = col + dy

                    if inGrid(x, y) and grid[x][y] == 1:
                        grid[x][y] = 2
                        num_oranges -= 1
                        queue.append((x, y))

            if not num_oranges:
                return cycles
        
        if num_oranges:
            return -1 
        return cycles