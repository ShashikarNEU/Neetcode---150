# https://neetcode.io/solutions/trapping-rain-water
# VERY TRICKY PROBLEM - Two pointer logic
# LOGIC
# for every index i, level of water at that index can be find out be min(left_max_before_i,right_max_after_i) - height[i]
# We need to apply this formula for every index using two pointers appoarch
# Have 2 pointers at both ends, if leftMax < rightMax, increment left pointer as WE ARE TRYING TO FIND THE MAX ON BOTH SIDES and vice versa. For that index(left or right pointer), we know that pointer max(left or right) is min. so, do leftmax or rightmax - height[index]. After finding that, you can update max by doing leftMax = max(leftMax, height[left]) or for right. WE NEED TO TAKE LEFT BEFORE THE INDEX AND RIGHTMAX AFTER THE INDEX. INDEX HEIGHT IS NOT COUNTED.

# Two Pointer Soln
class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]
        res = 0

        while left < right:
            if leftMax <= rightMax:
                left+=1
                waterLv = leftMax - height[left] if leftMax - height[left] > 0 else 0
                res += waterLv
                leftMax = max(leftMax, height[left])
            else:
                right-=1
                waterLv = rightMax - height[right] if rightMax - height[right] > 0 else 0
                res += waterLv
                rightMax = max(rightMax, height[right])
                
        return res

# 3 lists logic (Prefix, Suffix arrays method)
# we form 3 lists, leftMax, rightMax, minList and iterate through min list to find min[i] - height[i] and add it to res
# this method is easy compared to two pointer logic but has more SC(O(n))
class Solution:
    def trap(self, height: list[int]) -> int:
        leftMaxList = [0]*len(height)
        rightMaxList = [0]*len(height)
        leftMax = height[0]
        rightMax = height[len(height)-1]
        res = 0

        for i in range(len(height)):
            leftMaxList[i] = leftMax
            leftMax = max(leftMax, height[i])
        
        for i in range(len(height)-1,-1,-1):
            rightMaxList[i] = rightMax
            rightMax = max(rightMax, height[i])
        
        for i in range(len(height)):
            waterLv = min(leftMaxList[i], rightMaxList[i]) - height[i]
            res += waterLv if waterLv > 0 else 0
        
        return res
  
if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(s.trap([4,2,0,3,2,5]))