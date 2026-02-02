# For this question, we need to do it in logn time and it's already rotated sorted -> Binary Search
# Goal here is to find the break point, a[mid] > a[mid+1] and mid+1 will be the min since it's start of
# the sequence. Now, we need to find in which part the break point is, so, we comapare a[low], a[high] and a[middle]
# to find out which side the break point is
# Problem num arr format -> higher num lower nums [Because of rotation]
# Since we know that we have to compare a[low], a[high] and a[middle]. There are two cases here. 
# Case 1- when middle falls in higher num part 
# num[low] < num[midd] > num[high]

# Case 2- when middle falls in lower num part
# num[low] > num[midd] < num[high]

# for the Base case, compare middle with middle+1, if it's middle is greater, then return num[middle+1]
# (if nums[middle] >= nums[middle + 1])
class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums)-1
        # if nums is of size 1
        if len(nums) == 1:
            return nums[low]
        # if the arr is not rotated
        if nums[low] < nums[high]:
            return nums[low]

        while low < high:
            middle = (low+high)//2
            if nums[middle] > nums[middle+1]:
                return nums[middle+1]
            elif nums[middle] > nums[low] and nums[middle] > nums[high]:
                low = middle
            elif nums[middle] < nums[low] and nums[middle] < nums[high]:
                high = middle
        
        return -1

# Other Attempt
class Solution:
    def findMin(self, nums: list[int]) -> int:
        start = 0
        end = len(nums)-1

        # Length = 1, edge case
        if len(nums) == 1:
            return nums[0]

        # no rotation exists
        if nums[start] < nums[end]:
            return nums[start]

        while start < end:
            middle = (start+end)//2
            if nums[middle] > nums[start] and nums[middle] > nums[end]:
                start = middle
            elif nums[middle] < nums[start] and nums[middle] < nums[end]:
                end = middle
            elif nums[middle] > nums[middle+1]:
                return nums[middle+1]
        
        return -1

def main():
    test_cases = [
        [1, 2, 3, 4, 5],       # Already sorted
        [2, 3, 4, 5, 1],       # Single rotation
        [4, 5, 1, 2, 3], # Rotation in the middle
        [2, 1],                # Two elements, rotated
        [1,2],                # Two elements, not rotated
        [3, 1, 2],             # Three elements, pivot in the middle
        [1]
    ]
    s = Solution()
    
    for i, nums in enumerate(test_cases):
        print(f"Test Case {i+1}: {nums} -> Min: {s.findMin(nums)}")

if __name__ == "__main__":
    main()

