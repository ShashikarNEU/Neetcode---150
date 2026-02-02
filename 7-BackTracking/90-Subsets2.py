# Brute - Sort and use result set
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = set()
        nums.sort()
        def subset(index, arr):
            if index >= len(nums):
                result.add(tuple(arr))
                return
            
            arr.append(nums[index])
            subset(index+1,arr)
            arr.remove(nums[index])

            while index < len(nums) - 1 and nums[index] == nums[index+1]:
                index+=1
            
            subset(index + 1, arr)
        
        subset(0,[])
        result = [list(r) for r in result]
        return result

# Optimal - Sort and do while loop in backtracking to skip elements when arr[i] ==  arr[i+1]
class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        def subset(index, arr):
            if index >= len(nums):
                result.append(list(arr))
                return
            
            arr.append(nums[index])
            subset(index+1,arr)
            arr.remove(nums[index])

            # This piece of code avoids duplicates. in [1,2,2] it can give [1,2] and [1,2]. This will prevent that
            while index < len(nums) - 1 and nums[index] == nums[index+1]:
                index+=1
            
            subset(index + 1, arr)
        
        subset(0,[])
        
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([4,4,4,1,4]))