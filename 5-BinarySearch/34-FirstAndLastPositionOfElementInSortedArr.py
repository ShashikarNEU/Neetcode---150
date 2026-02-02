# Do the same old binary search but after reaching the num as middle, instead of putting num[middle] == target -> return middle
# you continue the while loop by putting nums[middle] >= target: high = middle-1, you go backwards if it's equal to find the leftmost boundary. do the same for right most boundary, if nums[middle] < target: low = middle + 1, you go forward till you find the rightmost boundary. Keep updating the leftbound and rightbound in while loop(it's middle not middle-1 or middle+1). if the value is not present in leftbound BS, return [-1,-1]
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Binary Search to find left most boundary
        low = 0
        high = len(nums)-1
        left_bound = -1

        while low <= high:
            middle = (low+high)//2

            if nums[middle] < target:
                low = middle + 1
            else:
                left_bound = middle
                high = middle - 1
        
        if left_bound == -1:
            return [-1,-1]
        
        if nums[left_bound] != target:
            return [-1,-1]
        
        # Binary Search to find the right most boundary
        low = 0
        high = len(nums)-1
        right_bound = -1

        while low <= high:
            middle = (low+high)//2

            if nums[middle] <= target:
                right_bound = middle
                low = middle + 1
            else:
                high = middle - 1
        
        return [left_bound, right_bound]


if __name__ == "__main__":
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10],8))
    print(s.searchRange([5,7,7,8,8,10],6))
        
        