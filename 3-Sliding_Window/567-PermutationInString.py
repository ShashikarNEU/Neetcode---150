from collections import defaultdict

# Fixed window - (You can use hashSet or hashTable)
# Have a fixed window and search the anagram in that fixed window(TC=26*n)
# for i in range(len(s2)-window+1): -> if len(s2) == window, loop never starts, so we put +1 in the loop [TRICKY]
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashTable_s1 = defaultdict(int)

        for str1 in s1:
            hashTable_s1[str1] += 1
        
        window = len(s1)
        for i in range(len(s2)-window+1):
            hashTable_s2 = defaultdict(int)
            for j in range(i,i+window):
                hashTable_s2[s2[j]] += 1
            if hashTable_s1 == hashTable_s2:
                return True
            hashTable_s2.clear()
        
        return False

# Using arr instead of hashTable
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr_s1 = [0]*26
        for s in s1:
            index = ord(s) - ord('a')
            arr_s1[index] += 1
        
        arr_s2 = [0]*26
        k = len(s1)
        n = len(s2)
        
        if k > n:
            return False
        
        for i in range(k):
            index = ord(s2[i]) - ord('a')
            arr_s2[index] += 1
        
        if arr_s1 == arr_s2:
            return True
        
        for i in range(n-k):
            index_remove = ord(s2[i]) - ord('a')
            index_add = ord(s2[i+k]) - ord('a')
            
            arr_s2[index_remove] -= 1
            arr_s2[index_add] += 1
            
            if arr_s1 == arr_s2:
                return True
        
        return False
        
if __name__ == "__main__":
  s = Solution()
  print(s.checkInclusion("ab","eidbaooo"))
  print(s.checkInclusion("ab","eidboaoo"))
                
        
