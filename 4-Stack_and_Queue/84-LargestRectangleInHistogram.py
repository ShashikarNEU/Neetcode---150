# https://neetcode.io/solutions/largest-rectangle-in-histogram
# Do a dry run and watch video first!!
# Monotonically increasing stack
# Maintain the stack as increasing, if nums[i], pop everything untill the codn is maintained

# Now, area calculation is the tricky part here
# when popping off elements, caculate the popped element area, take the index of the popped element and find the distance(index-i(element that is <))*popped element height. find maxarea from this.
# for the element that is < when adding it to the stack after popping off everything that is >, add the last popped element index as the < element index in the stack(Watch video or do a dry run for explanation)[We can compute the area backwards also]

# For the remaining elements in the stack, since we can extend till the end find max(height[i]*(len(heights)-i)) in the stack
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] # index, height
        maxArea = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            
            stack.append((start, heights[i]))
        
        for i in range(len(stack)):
            maxArea = max(maxArea, stack[i][1]*(len(heights)-stack[i][0]))
        
        return maxArea


if __name__ == "__main__":
  s = Solution()
  print(s.largestRectangleArea([2,1,5,6,2,3]))
  print(s.largestRectangleArea([2,4]))
