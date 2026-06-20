# Think this question in two pointers way
# since brute force is n3, we can sort for free(n2)
# then apply for-loop and inside that for-loop, sorted two sum
from ast import List
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        nums.sort()
       
        for i in range(len(nums)):
            p1 = i+1
            p2 = len(nums)-1
            while p1 < p2:
                sum = nums[p1] + nums[p2] + nums[i]
                if sum == 0:
                    result.add(tuple([nums[p1],nums[p2],nums[i]]))
                if sum < 0:
                    p1+=1
                else:
                    p2-=1
        return [list(i) for i in result] # set of tuples to list of list

# This is the solution that you should be aiming for
# you will forget about duplicates, so recall about that
# and for skipping duplicates, you have to be to concerned with it only when adding to the result arr(when sum == 0 case)
# because that's the case, we will add duplicates to the res arr. you also need to skip duplicates on the outer loop also 
# so that we won't do the same work again. For sum < 0, sum > 0, duplicates don't matter because we are not adding them to res arr
# We will manually check them one by one
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            start = i+1
            end = len(nums)-1
            
            while start < end:
                sum = nums[i]+nums[start]+nums[end]
                if sum < 0:
                    start+=1
                elif sum > 0:
                    end-=1
                else:
                    result.append([nums[i],nums[start],nums[end]])

                    while start < end and nums[start] == nums[start+1]:
                        start+=1
                    while start < end and nums[end] == nums[end-1]:
                        end-=1
                    
                    start+=1
                    end-=1
        
        
        return result

    
if __name__ == "__main__":
    s = Solution()
    list1 = [-1,0,1,2,-1,-4]
    print(s.threeSum(list1))
                        