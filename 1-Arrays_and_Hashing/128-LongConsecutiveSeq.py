# Brute force -> O(n2) time
# convert it into set, for every number I am checking for a seq and recording the longest sequence
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashSet = set(nums) # to access elements in O(1) time
        stepUp = False
        count = 1
        result = 0
        for i in hashSet:
            if i+1 in hashSet:
                stepUp = True
            else:
                stepUp = False
          
            while True:
                if stepUp:
                    if i+1 in hashSet:
                        count+=1
                        i+=1
                    else:
                        if count > result:
                            result = count
                        count = 1
                        break
                else:
                    if i-1 in hashSet:
                        count+=1
                        i-=1
                    else:
                        if count > result:
                            result = count
                        count = 1
                        break
        return result

# for the optimal solution
# VERY IMP -> PLS ITERATE THROUGH THE HASH SET not normal nums
# You check for start of a sequence and only look for a seq from there
# if you encounter something middle of the seq, you don't do anything and skip it
# you find the start of the sequence by checking if the i-1 does not exist in the set
# remove duplicates because they don't affect the soln so, iterate over a set
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hashSet = set(nums) # to access elements in O(1) time
        count = 1
        result = 0
        for i in hashSet:
             if i-1 in hashSet:
              continue
             else:
                while i+1 in hashSet:
                  count+=1
                  i+=1
                result = max(result, count)
                count = 1
        return result
    
# CODING TRICKS
# for while loop, when you can't think of a exit condn
# Put the if codn inside the while as the exit codn for while -> coding will become easy
        