# If you use the same appoarch as word search 1, you will get TLE Error or visited set wrong ans
# Brute force TC O(M*N*words*4^(m*n)) and SC O(m*n)

# you will have to clear visited set also bw different words
# Passing 43/65 test cases only
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        ROW = len(board)
        COL = len(board[0])

        visited = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row, col, index, word, visited):
            if row < 0 or col < 0 or row>=ROW or col >=COL:
                return False
            if (row, col) in visited:
                return False
            
            if board[row][col] != word[index]:
                return False
            
            if index == len(word)-1:
                return True
            visited.add((row,col))
            for r,c in directions:
                if dfs(row+r,col+c, index+1, word, visited):
                    visited.remove((row,col))
                    return True
            visited.remove((row,col))
            return False
        
        result = set()
        for i in range(ROW):
            for j in range(COL):
                for word in words:
                    if board[i][j] == word[0]:
                        if dfs(i,j,0,word, set()):
                            result.add(word)
                        
        return list(result)

# Optimal - Trie
            
            
            


        