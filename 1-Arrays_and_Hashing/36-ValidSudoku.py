# LOGIC
# Look at the three rules here. Check each rows and cols for duplicates, you can use hashTable or hashSet here.
# For checking 3*3 grids of the sudoku, classify (0,8) -> i and (0,8) -> j into (0,2)(0,2) hashTable, value of the hashTable is a set
# so, youy will have 9 sets. keys of the hashTable are (row//3,col//3) not % but //. when encountering . skip it(continue).

from ast import List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = len(board)
        COL = len(board[0])
        
        # CHECKING ROW WISE
        for r in range(ROW):
            rowSet = set()
            for c in range(COL):
                if board[r][c] != '.':
                    if board[r][c] in rowSet:
                        return False
                    rowSet.add(board[r][c])
        
        # CHECKING COL WISE
        for c in range(COL):
            colSet = set()
            for r in range(ROW):
                if board[r][c] != '.':
                    if board[r][c] in colSet:
                        return False
                    colSet.add(board[r][c])
        
        # CHECKING 9*9 SIZE
        hashSet = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] != '.':
                    if board[r][c] in hashSet[r//3][c//3]:
                        return False
                    hashSet[r//3][c//3].add(board[r][c])
        
        return True

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]))
    
    print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]))

      

            