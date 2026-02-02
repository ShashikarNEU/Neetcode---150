# Apply normal binary search but go after the greater element
# if nums[mid] > nums[mid+1] go after mid so, high = mid - 1 and vice versa
# if mid == n-1, end of the arr, then return that as answer[THINK]

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low = 0
        high = len(nums)-1
        n = len(nums)-1

        if len(nums) == 1:
            return 0

        while low <= high:
            mid = (low+high)//2

            if mid < n and nums[mid] >= nums[mid+1]:
                high = mid-1
            elif mid < n and nums[mid] < nums[mid+1]:
                low = mid+1
            else:
                return mid
        
        return low
        