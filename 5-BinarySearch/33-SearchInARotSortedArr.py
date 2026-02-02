# This is a follow up to 153 leetcode - find min in a rotated sorted arr
# First we find the middle(break point) and split the arr up and apply binary search on the 2 halfs
# to find the index
class Solution:
    def findMiddle(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        if nums[low] < nums[high]:
            return low
        if len(nums) == 1:
            return 0
        while low <= high:
            middle = (low+high) // 2
            if nums[middle] >= nums[middle + 1]:
                return middle
            if nums[middle] > nums[high] and nums[middle] > nums[low]:
                low = middle
            elif nums[middle] < nums[low] and nums[middle] < nums[high]:
                high = middle
        return -1
    
    def binary_search(self, nums: list[int], target: int) -> int:
      low = 0
      high = len(nums) - 1
      while low <= high:
        middle = (low + high) // 2
        if nums[middle] == target:
          return middle
        if nums[middle] < target:
          low = middle + 1
        else:
          high = middle - 1
      return -1
    
    def search(self, nums: list[int], target: int) -> int:
        middle = self.findMiddle(nums)
        index = -1
        if len(nums) == 1 and nums[0] == target:
           return 0
        indexl = self.binary_search(nums[0:middle+1], target)
        indexr = self.binary_search(nums[middle+1:], target)
        if indexl != -1:
           return indexl
        elif indexr != -1:
           return indexr + middle + 1
        else:
           return -1

if __name__ == "__main__":
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))
           
           

        