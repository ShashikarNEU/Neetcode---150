# https://neetcode.io/solutions/n-queens
# We are taking only row or col as argument and iterating through the other one
# keep a recursive call, for c in col: backtrack(row+1). Termination codn is if the row reaches n then, append to result in required fmt
# To keep track of the attacked row,col, use 3 things, row only one is guarntted. Keep a placed queens col set, negative diagonals set
# positive diagonals set. 
# When we place a queen, we can draw, +ve and -ve diagonals from the placed queen. +ve diagonal's (r+c) value will be constant across the whole diagonal and -ve diagonal's (r-c) value will be constant across the whole diagonal. So, When we get to that value, just check (r+c) and (r-c) for +ve/-ve diagonal if it's in the set and check if col in col set also.
# if not, place a queen there and add +ve,-ve values recur call. After termination, after reaching the goal, in backtrack, remove board position and that +ve and -ve diagonal for exploring other col in that row.

# Don't do shallow copy - it copies the outer list not the inner list
# So, inside cols within rows will still be shared(address memory)
# Use a Deep Copy instead, iterate the whole board and create a new list to add to the output
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.']*n for _ in range(n)]
        positive_digonals = set() # r+c(upwards diagonal)
        negative_diagonals = set() # r-c(downwards diagonal)
        placed_queens_col = set() # Will only track col because rows, we are transvering one by one
        result = []

        def backtrack(row):
            if row == n:
                required_fmt = ["".join(row) for row in board]
                result.append(required_fmt)
                return
            
            for col in range(n):
                if col in placed_queens_col or (row+col) in positive_digonals or (row-col) in negative_diagonals:
                    continue
                
                placed_queens_col.add(col)
                positive_digonals.add(row+col)
                negative_diagonals.add(row-col)
                board[row][col] = 'Q'

                backtrack(row+1)

                board[row][col] = '.'
                placed_queens_col.remove(col)
                positive_digonals.remove(row+col)
                negative_diagonals.remove(row-col)

        backtrack(0) # starting from row 0
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))