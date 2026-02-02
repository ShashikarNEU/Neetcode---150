# Think this question in two pointers way
# since brute force is n3, we can sort for free(n2)
# then apply for-loop and inside that for-loop, sorted two sum
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

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res: list[list[int]] = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return res

    
if __name__ == "__main__":
    s = Solution()
    list1 = [-1,0,1,2,-1,-4]
    print(s.threeSum(list1))
                        