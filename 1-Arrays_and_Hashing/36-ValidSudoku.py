# LOGIC
# Look at the three rules here. Check each rows and cols for duplicates, you can use hashTable or hashSet here.
# For checking 3*3 grids of the sudoku, classify (0,8) -> i and (0,8) -> j into (0,2)(0,2) hashTable, value of the hashTable is a set
# so, youy will have 9 sets. keys of the hashTable are (row//3,col//3) not % but //. when encountering . skip it(continue).

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
      ROW = len(board)
      COL = len(board[0])

      # For checking rows
      for i in range(ROW):
         # Hashset for checking duplicates in each row
         hashSetRow = set()
         for j in range(COL):
            if board[i][j] == '.':
               continue
            if board[i][j] in hashSetRow:
               return False
            hashSetRow.add(board[i][j])
      
      # For checking cols
      for j in range(COL):
         # Hashset for checking duplicates in each row
         hashSetCol = set()
         for i in range(ROW):
            if board[i][j] == '.':
               continue
            if board[i][j] in hashSetCol:
               return False
            hashSetCol.add(board[i][j])
      
      # For checking 3*3 grids
      hashTable = defaultdict(set)
      for i in range(ROW):
         for j in range(COL):
            if board[i][j] == '.':
               continue
            r = i//3
            c = j//3
            if board[i][j] in hashTable[(r,c)]:
               return False
            hashTable[(r,c)].add(board[i][j])
      
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

      

            