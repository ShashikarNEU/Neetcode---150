# https://neetcode.io/solutions/word-ladder
# Basic logic, make a graph with words and edge with one letter difference each word and then find the shortest path from start word
# to end word. Shortest path -> Use BFS. Now, making that graph is the question. you can use n2*m apporach to make it but it won't pass all cases in leetcode
# So, to efficiently do it, make a pattern for each word -> Hit, patterns - *it, h*t, hi* and put hit as value with patterns as keys
# this will be your new adj list. To make this, we need n*m*m time. Then do minute BFS(Refer rotting oranges question or neetcode way - loop for all queue elements inside while queue loop). BFS time -> n2*m (since max number of edges are n2 for n nodes)
# Total time -> n*m2 * (n2*m) = n3m3
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Have a dict to store pattern and edges
        adj_list = {}
        # Make a graph with connecting edges - hot -> hit forms a edge because of one letter difference
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                if pattern not in adj_list:
                    adj_list[pattern] = []
                adj_list[pattern].append(word)
        
        # if you want to access a neighbour of a node, create all patterns of that node and search in the dict (for hit -> *it,h*t,hi* search in dict with these keys)

        # Now, do BFS
        queue = deque()
        visited = set()
        visited.add(beginWord)
        queue.append(beginWord)
        queue.append(None)
        count = 1 # count from begin word

        while queue:
            word = queue.popleft()

            if word == endWord:
                return count

            if not word:
                if queue:
                    queue.append(None)
                count += 1
                continue
            
            
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbour_words = adj_list[pattern]
                for neighbour_word in neighbour_words:
                    if neighbour_word not in visited:
                        visited.add(neighbour_word)
                        queue.append(neighbour_word)
          
        return 0

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
                


