from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def inBoard(r, c, i):
            if 0 <= r < rows and 0 <= c < cols and i < len(word) and board[r][c] == word[i]:
                return True
            return False

        def found(i):
            return i == len(word) - 1
        
        def dfs(r: int, c: int, idx: int) -> bool:
            if not inBoard(r, c, idx):
                return False
            if found(idx):
                return True
            
            temp = board[r][c]
            board[r][c] = '*'

            for x, y in directions:
                if dfs(x + r, y + c, idx + 1):
                    return True
            
            board[r][c] = temp
            return False


        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False

