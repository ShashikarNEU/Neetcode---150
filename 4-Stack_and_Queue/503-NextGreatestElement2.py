# [Monotonic Stack Pattern] 
# Here, unique elements are not gauntereed
# So, put indexes in stack and pop them, use index to find the value(nums[index])
# Use monotonic stack here, but only put the index inside stack if i < n(first skip)
# since it's circular, (put i=i%n) and do 2 loop (range(2*n)). for only while stack and nums[i] > nums[stack[-1]]: will called in the second iteration, if nums[i] voilates monotoc stack codn, then pop it and assign the res[index] -> to that value
# [1,2,3,4,3] -> Take this example and do a dry run, you will understand why two iterations are required
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        res = [-1]*len(nums)
        stack = []
        
        for i in range(2*len(nums)):
            i = i % len(nums)
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                res[index] = nums[i]
            if i < len(nums):
                stack.append(i)
        
        return res

if __name__ == "__main__":
  s = Solution()
  print(s.nextGreaterElements([1,2,1]))
  print(s.nextGreaterElements([1,2,3,4,3]))


            