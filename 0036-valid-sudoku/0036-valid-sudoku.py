class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols = len(board), len(board[0])
        
        row = {r : set() for r in range(rows)}
        col = {c : set() for c in range(cols)}
        three_by = {sq : set() for sq in range(9)}
        
        col_nav = {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 1,
            4 : 1,
            5 : 1,
            6 : 2,
            7 : 2,
            8 : 2
        }

        row_nav = {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 3,
            4 : 3,
            5 : 3,
            6 : 6,
            7 : 6,
            8 : 6
        }
        
        for r in range(rows):
            for c in range(cols):
                val = board[r][c]
                if val == ".":
                    continue
                if val in row[r] or val in col[c]:
                    return False
                sq = row_nav[r] + col_nav[c]
                if val in three_by[sq]:
                    return False
                
                row[r].add(val)
                col[c].add(val)
                three_by[sq].add(val)
        return True
