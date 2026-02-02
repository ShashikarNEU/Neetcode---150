# This question follows the same pattern as print all sequences but here, you can print a num multiple times
# so for each num, pick same num, same index f(index, result - arr[index]) and go to the next num and don't pick the same num
# so, f(index+1, result)
# Pattern also follows pick or don't pick for a single num
# Base cases -> if target < 0 return and index >= length of arr return if target == 0 append to result and return
# when target == 0, append the copy of the arr to result and return,because list is a reference
from typing import List


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        def com_sum(index, arr, total):
            if total == target:
                result.append(list(arr))
                return
            if index >= len(candidates) or total > target:
                return
            arr.append(candidates[index])
            com_sum(index, arr, total + candidates[index])
            arr.remove(candidates[index])
            com_sum(index + 1, arr, total)
        com_sum(0, [], 0)
        return result
    
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        arr = []
        def comSum(i, target):
            if target == 0 and i == len(candidates):
                res.append(arr.copy())
                return
            if target < 0 or i >= len(candidates):
                return
            arr.append(candidates[i])
            comSum(i, target-candidates[i])
            arr.pop()
            comSum(i+1, target)
        
        comSum(0,target)
        return res

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,5], 8))