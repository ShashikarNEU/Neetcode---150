# Brute Force
# Find all sub arr and check if the sum is k
# TC -> N^2
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                #nums[i:j+1] -> sub arr
                sum += nums[j]
                if sum == k:
                    count+=1
        return count

# TRICKY SOLN
# Optimal - prefix arr + two sum(hashMap)
# Using prefix arr and finding diff bw two nums[i], you can find sub arr sums
# Use prefix arr and find all sub arr sums from there
# but this alone is not enough
# We use two sum - hashMap here also
# from prefix arr (we need to find b - a = target)
# or a = b - target
# Have a hashmap and search for b-target(a) in here
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix = defaultdict(int)
        sum = 0
        count = 0
        prefix[0] = 1 # This handles when sum == k case(no difference case)
        for i in range(len(nums)):
            sum+=nums[i]
            if sum - k in prefix:
                count += prefix[sum-k]
            prefix[sum] += 1
        return count
                
# Test cases
if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1,1,1],2))
    print(s.subarraySum([1,2,3],3))
    
    