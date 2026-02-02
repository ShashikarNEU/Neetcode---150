# https://leetcode.com/problems/valid-anagram/
# Here Brute force method will be to sort a string and equate them => (O(nlogn), O(1))
# Time - O(m+n) m=len(Str1),n=len(Str2) Space - O(1) because letters are max 26 only so, hashtable will be that long
class Solution:
    def createHashTable(self, nums) -> "dict":
        hashTable = {}
        for i in nums:
            if i in hashTable:
                hashTable[i] += 1
            else:
                hashTable[i] = 1
        return hashTable
            
    def isAnagram(self, s: str, t: str) -> bool:
        hashTable_s = self.createHashTable(list(s))
        hashTable_t = self.createHashTable(list(t))
        print(hashTable_s)
        print(hashTable_t)
        
        return hashTable_s == hashTable_t
        