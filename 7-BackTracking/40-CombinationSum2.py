# Brute Force - 172/175 test cases passed
# Use result set and sort the output when base case happens
class Solution:
    def combinationSum2Brute(self, candidates: list[int], target: int) -> list[list[int]]:
        result = set()
        def com_sum2(index, target, arr):
            if target == 0:
                result.add(tuple(sorted(arr)))
                return
            if target < 0 or index >= len(candidates):
                return
            
            arr.append(candidates[index])
            com_sum2(index+1, target - candidates[index], arr)
            arr.remove(candidates[index])
            com_sum2(index+1, target, arr)
        
        com_sum2(0, target, [])
        
        result = [list(rs) for rs in result]
        return result

# Optimal Soln
# Follow the same procedure as brute but for second recursion, when backtracking if it's the same variables we can avoid it using while loop, this is happens when back tracking goes to the front [1,1,1,2] in index 1, this happens during backtrack
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        def com_sum2(index, target, arr):
            if target == 0:
                result.append(list(arr))
                return
            if target < 0 or index >= len(candidates):
                return
            
            arr.append(candidates[index])
            com_sum2(index+1, target - candidates[index], arr)
            arr.remove(candidates[index])

            # for [1,1,1,1,1,1,2] while loop is useful to skip repeat combinations[Good way] - This will happen deep in recursion
            # This piece of code avoids duplicates. in [1,2,2] it can give [1,2] and [1,2]. This will prevent that
            while index < len(candidates)-1 and candidates[index] == candidates[index+1]:
                index+=1
            com_sum2(index+1, target, arr)
        
        com_sum2(0, target, [])
          
        return result

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([2,5,2,1,2], 5))