# This is similar to graph dfs
# https://neetcode.io/solutions/word-search (not refered video when doing this!)
# Use recursion to travel 4 sides(Up, Down, Right, Left), work with index, when word[index] != board[r][c] return False and after that if it's last index and equal then return True -> Keep giving True in backtrack. Use visited set and in back track remove the visited node
# TIP - Do everything at the top(when it enters recursion, not before the recursion)
# Run dfs on every node and if word[0] == board(i,j)

# Logic thinking -> if nr,nc in 4 directions not equal, remove (row,col) from visited, then it will backtrack

# TC = 4^n (approx), SC = n
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()

        def dfs(row, col, index):
            if (row, col) in visited:
                return False
            if board[row][col] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            visited.add((row, col))
            # if it's equal, go 1 index forward
            index+=1
            for r,c in directions:
                new_row, new_col = r + row, c + col
                if new_row < 0 or new_col < 0 or new_row >= ROW or new_col >= COL:
                    continue
                if dfs(new_row, new_col, index):
                    return True
            visited.remove((row, col))
            return False
            
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == word[0]:
                    if dfs(i,j,0):
                        return True
        
        return False

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
            
