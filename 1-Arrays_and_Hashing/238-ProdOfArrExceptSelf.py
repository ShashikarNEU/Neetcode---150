# https://leetcode.com/problems/product-of-array-except-self/description/
# Brute force - use nested for loop -> O(n2)
# use division and divide the product by a[i] - O(n)
# Optimal appoarch - use prefix and postfix mul arr

# Optimal appoarch
# Imagine mul prefix and postfix arr for every i, expect that i, cum mul of index i-1(prefix - from 0 to i-1) * cum mul of i+1(postfix - from n to i+1)
# Time - O(n) Space - O(n)
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefixArr = [] 
        postfixArr = [] 
        result = []
        prefixR = 1
        postfixR = 1

        for i in range(len(nums)):
            prefixR *= nums[i]
            prefixArr.append(prefixR)

        for i in range(len(nums)-1,-1,-1):
            postfixR *= nums[i]
            postfixArr.append(postfixR)

        postfixArr.reverse()
        print(prefixArr)
        print(postfixArr)

        for i in range(len(nums)):
            a = 1 if i-1 < 0 else prefixArr[i-1] 
            b = 1 if i+1 > len(nums)-1 else postfixArr[i+1]
          
            result.append(a * b)
        return result
  
# Most optimal solution 
# Use the same prefix and postfix technique but space should be O(1) - use the input and result arr only
# Input Arr -> Prefix Arr
# Res Arr -> Postfix Arr
# Find postfix arr first and then find prefix arr
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        prefixR = 1
        postfixR = 1

        for i in range(len(nums)):
            prefixR *= nums[i]
            result.append(prefixR)
        
        for i in range(len(nums)-1,-1,-1):
            postfixR *= nums[i]
            nums[i] = postfixR
        # print(nums)
        # print(result)
          
        for i in range(len(nums)):
            a = 1 if i-1<0 else result[i-1]
            b = 1 if i+1>len(nums)-1 else nums[i+1]
            #print(f"a:{a} b:{b}")

            nums[i] = a * b
      
        return nums
            
            
        


            
  

            
            
            
        