# Main Logic

# Remember all words are already sorted in lexographic order
# So, in edge creation, comparing i and i+1 element is enough
# 3 cases for edge creation
# case 1- app, apple
# no edge added
# case 2- apn, apple also (nr, gfe)
# will add n -> p edge here or n -> g
# case 3: apple, app
# Will return "" as answer because this lex order is wrong

# For adj list, we need a all words present as keys without repeation so, do 
# adj_list = [w: set() for word in words for w in word]
# this will give all unique words as keys because keys are unique and will assign a set to them

# After creating adj list, we need to print it in any acceptable order(DFS order won't work here)
# Use Topological order

class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        adj_list = {c: set() for w in words for c in w}
        # Edge Creation
        for i in range(len(words)-1):
            wordA = words[i]
            wordB = words[i+1]

            l1 = len(wordA)
            l2 = len(wordB)

            if l1 > l2:
                for j in range(l2):
                    if wordA[j] != wordB[j]:
                        adj_list[wordA[j]].add(wordB[j])
                        break
                    
                    if j == l2 - 1:
                        return ""
            else:
                for j in range(l1):
                    if wordA[j] != wordB[j]:
                        adj_list[wordA[j]].add(wordB[j])
                        break
        
        print(adj_list)
        visited = set()
        cycle = set()
        result = []
        def dfs(source):
            if source in visited:
                return True
            if source in cycle:
                return False
            cycle.add(source)
            nodes = adj_list[source]
            for node in nodes:
                if not dfs(node):
                    return False
            cycle.remove(source)
            visited.add(source)
            result.append(source)
            return True
        
        nodes = adj_list.keys()
        print(nodes)
        for node in nodes:
            if node not in visited:
                if not dfs(node):
                    return ""
        
        result.reverse()
        return "".join(result)

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.foreignDictionary(["z","o"]))
    print(s.foreignDictionary(["hrn","hrf","er","enn","rfnn"]))
            
                    
                
                        
