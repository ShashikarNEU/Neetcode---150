from collections import defaultdict
# https://neetcode.io/solutions/next-greater-element-i

# Using hashTable
# n2 soln
# Appoarch the question from num2 and have a hashTable on num1
# First have hashTable record everything in nums1, value -> index
# for num2, check if it's in num1 and do n2 appoarch, once you find the next greatest element, do break. and you have to assign it in index where element was in num1(Hence the hashMap). if result index is empty, put -1
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashTable = defaultdict(int)
        for i in range(len(nums1)):
            hashTable[nums1[i]] = i
        
        res = [0]* len(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] in hashTable:
                index = hashTable[nums2[i]]
                for j in range(i+1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        res[index] = nums2[j]
                        break
                if res[index] == 0:
                    res[index] = -1
        return res

# Using Stack
# Monotonically Decreasing Stack Apporach(Same pattern as max sliding window problem)
# [4,1,2] and [2,1,3,4]
# Take ipad and draw the algo for this exmaple, you will understand it easily
# After finishing the loop in num2, some items will be left in the stack. Go through them and if they appear in  num1, find index, put value as -1 since there is no next element
# instead of putting -1 in the last, we can declare res array with -1 for everything in the start[CLEVER]
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashTable = defaultdict(int)
        for i in range(len(nums1)):
            hashTable[nums1[i]] = i
        
        res = [0]*len(nums1)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                num = stack.pop()
                index = hashTable[num]
                res[index] = nums2[i]
            
            if nums2[i] in hashTable:
                stack.append(nums2[i])
        
        for num in stack:
            index = hashTable[num]
            res[index] = -1
        
        return res
            
if __name__ == "__main__":
  s = Solution()
  print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
  print(s.nextGreaterElement([2,4], [1,2,3,4]))
