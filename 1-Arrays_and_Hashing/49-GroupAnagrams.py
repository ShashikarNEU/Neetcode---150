# https://leetcode.com/problems/group-anagrams/
# Brute Force Solution
# Here I am just sorting the strings and building a hashtable to record them
# Key - Sorted String, Values - array of anagrams
# m = list length and n=longest string length
# Time - O(mnlogn) sort string=nlogn, m is the list length, Space - O(m)
from collections import defaultdict


class Solution:
    def sortString(self, string: str) -> str:
        list = sorted(string)
        return "".join(list)
        
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashTable = {}
        result = []
        for str in strs:
            sortedString = self.sortString(str)
            if sortedString in hashTable:
                hashTable[sortedString].append(str)
            else:
                hashTable[sortedString] = []
                hashTable[sortedString].append(str)
        
        for arr in hashTable.values():
            result.append(arr)
        
        return result

# Optimized approach
# Use a array to record the letters(a-z 26 letters) then use that array as a key in the hashmap to group the anagrams as values
# in a dict in python, we can use tuple as an key(not a another dict or a array)
# Time - O(m*n) Space - O(m) m = list length and n=longest string length
class Solution:
    def createLettersArr(self, nums) -> "list":
        array = [0]*26
        for num in nums:
            index = ord(num) - ord('a')
            array[index]+=1
        return array
        
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashTable = {}
        result = []
        for str in strs:
            arr = self.createLettersArr(list(str))
            key = tuple(arr)
            if key in hashTable:
                hashTable[key].append(str)
            else:
                hashTable[key] = []
                hashTable[key].append(str)
        
        for arr in hashTable.values():
            result.append(arr)
        
        return result

# Same apporach (diff attempt)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashTable = defaultdict(list)
        for str in strs:
            a = [0]*26
            for s in str:
                index = ord(s) - ord('a')
                a[index]+=1
            hashTable[tuple(a)].append(str)
        return list(hashTable.values())
        

        

        