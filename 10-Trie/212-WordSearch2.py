# https://neetcode.io/solutions/word-search-ii

# Use Trie + DFS logic
# DFS Logic is similar to word search 1
# Add trie, create trie class and add every word into a trie
# for each cell in the board, compare it with trie and movie forward in trie and matrix
# if all words are equal and endOfWord = True then add to result set. use set cuz there can be duplicates
class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
    def insert(self,word):
        curr = self # since root is not there
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endOfWord = True
            
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for word in words:
            root.insert(word)
            
        ROW = len(board)
        COL = len(board[0])

        visited = set()
        result = set() # In case of duplicates

        def dfs(row, col, node, word):
            if row < 0 or row >= ROW or col < 0 or col >= COL or (row,col) in visited or board[row][col] not in node.children:
                return
            
            visited.add((row,col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.endOfWord:
                result.add(word)

            # Can use a for loop also here(Same thing!!)
            dfs(row+1, col, node, word)
            dfs(row, col+1, node, word)
            dfs(row-1, col, node, word)
            dfs(row, col-1, node, word)

            visited.remove((row,col))
        
        for i in range(ROW):
            for j in range(COL):
                dfs(i,j,root,"")
        
        return list(result)