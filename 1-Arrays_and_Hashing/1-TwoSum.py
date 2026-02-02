#https://leetcode.com/problems/two-sum/
# we know that a+b = target so use, b = target - a, 
# do target - a for every element and use hashTable if b exists immediately
# Do it in one loop because target - a index should not be same index as b, it will pick the same element twice so, Assign hashTable index later Think about this case [3,2,4,1] Target = 6
# Time - O(n), Space - O(n)
from collections import defaultdict


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashTable={}
        for index, num in enumerate(nums):
            b = target - num
            if b in hashTable:
                return [index, hashTable[b]]
            hashTable[num] = index

# defaultdict soln
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashTable = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in hashTable:
                return [i, hashTable[target - nums[i]]]
            hashTable[nums[i]] = i
          