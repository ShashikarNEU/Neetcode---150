# https://leetcode.com/problems/top-k-frequent-elements/description/
# Question meaning -> k means means of output they want, k=2 means they want top 2 repeating nums
# Brute force - make a hashtable and sort them acc to the values and return the top k keys
# Time - O(nlogn) Space - O(n)
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashTable = {}
        result = []
        for num in nums:
            if num in hashTable:
                hashTable[num]+=1
            else:
                hashTable[num]=1
      
        sortedHashTable = dict(sorted(hashTable.items(), key = lambda item : item[1], reverse = True))

        for i in sortedHashTable.keys():
            result.append(i)
        
        return result[:k]

# Optimal appoarch - Use Array
# Make a hashTable and use a 2d array. Use the array index as no of repeating times for a number, repeating number times can't be more than size of the input array
# Array should have k+1 indexes because all elements are same, count will be k but index will be from 0 to k-1
# Then from the last return k elements as the answer
# Time - O(n), Space - O(n)

class Solution:               
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashTable = {}
        # Length of the count arr should be same as nums(edge case- if all nums are same)
        countArr = [[] for i in range(0,len(nums)+1)] # Two numbers can have the same count
        result = []
        for num in nums:
            if num in hashTable:
                hashTable[num]+=1
            else:
                hashTable[num]=1
        
        for key, value in hashTable.items():
            countArr[value].append(key)
            
        for i in countArr:
            for j in i:
                result.append(j)
                
        return result[-k:]

# Diff attempt - using defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        a = [[] for _ in range(len(nums)+1)]
        hashTable = defaultdict(int)

        for num in nums:
            hashTable[num]+=1
        
        
        for key, value in hashTable.items():
            a[value].append(key)

        result = []
        for nums in a:
            for num in nums:
                result.append(num)
        return result[-k:]