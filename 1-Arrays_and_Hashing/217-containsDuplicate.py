#https://leetcode.com/problems/contains-duplicate/
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashTable = {}
        for i in nums:
            if i in hashTable:
                hashTable[i] += 1
                return True
            else:
                hashTable[i] = 1
        return False

# Defaultdict soln
class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashTable = defaultdict(int)
        for i in range(len(nums)):
            hashTable[nums[i]] += 1
            if hashTable[nums[i]] == 2:
                return True
        return False