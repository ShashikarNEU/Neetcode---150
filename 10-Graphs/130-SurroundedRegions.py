# [MAIN LOGIC] -> We can only change O to X if all O are surrounded by X. if it's in the boundary 
# then, that whole island of O's cannot be converted to X. 

# So, take O along the boundaries and do BFS/DFS on those O's and put them in a visited set. if O in visited set then
# we cannot change the O to X. for every other O, change it to X.
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROW = len(board)
        COL = len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visited = set()

        def dfs(r, c):
            if (r,c) in visited:
                return
            if r < 0 or c < 0 or r >= ROW or c >=COL or board[r][c] == "X":
                return
            
            visited.add((r, c))

            for row, col in directions:
                dfs(r + row, c + col)
        
        for c in range(COL):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROW-1][c] == "O":
                dfs(ROW-1,c)
        
        for r in range(1,ROW-1):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][COL-1] == "O":
                dfs(r, COL-1)
         
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and board[r][c] == "O":
                    board[r][c] = "X" 

# Call the test function
if __name__ == "__main__":
    s = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    s.solve(board)
    print(board)

    board2 = [["X"]]
    s.solve(board2)
    print(board2)