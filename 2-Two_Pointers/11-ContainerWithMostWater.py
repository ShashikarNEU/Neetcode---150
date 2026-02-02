# Looking at this problem, I can find out that it must be sliding window or two pointer pattern
# Try sliding window method, you won't be able to find the sliding codn 
# Try two pointer with p1 and p2 being at opp ends, pointer moving codn is comparing the arr[p1]
# and arr[p2] if arr[p1] is greater, then move the p2 pointer in hope of finding a greater value because we want to min(arr[p1],arr[p2]) to be max. Take care of the window length also
class Solution:
    def maxArea(self, height: list[int]) -> int:
        p1 = 0
        p2 = len(height) - 1
        window = len(height) - 1
        maxArea = 0
        area = 0
        while p1 < p2:
            area = min(height[p1],height[p2]) * window
            maxArea = max(maxArea, area)
            if height[p1] < height[p2]:
                p1+=1
            else:
                p2-=1
            window-=1
        return maxArea