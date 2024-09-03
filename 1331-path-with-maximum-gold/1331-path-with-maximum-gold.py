class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # match
        # dfs 

        # plan
        # iterate through grid
        # if cell > than 0 dfs on cell
        # check if the cell is valid
        # mark cell as visited storing value in a temp variable
        # iterate through the directions updating max gold
        # return max gold + the temp variable 
        # unmark the cell and return 

        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        def inGrid(r: int, c: int) -> bool:
            if 0 <= r < rows and 0 <= c < cols:
                return True
            return False
        
        def dfs(r: int, c: int) -> int:
            if not inGrid(r, c) or grid[r][c] == 0:
                return 0
            
            temp = grid[r][c]
            grid[r][c] = 0

            curr_gold = 0
            for x, y in directions:
                curr_gold = max(curr_gold, dfs(r + x, c + y))
            
            grid[r][c] = temp
            return curr_gold + temp
        
        max_gold = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    max_gold = max(dfs(r, c), max_gold)
        return max_gold


