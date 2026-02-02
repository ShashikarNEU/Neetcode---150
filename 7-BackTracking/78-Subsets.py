# Subsets and subsequences are almost same but subsets does not follow order but subsequence follows order
# but algo for both is the same, since we are starting from index 0 and following order till n
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def subset(index, res):
            if index >= len(nums):
                result.append(list(res))
                return
            res.append(nums[index])
            subset(index + 1, res)
            res.remove(nums[index])
            subset(index + 1, res)
        subset(0, [])
        return result

# Other Attempt (You can declare arr at a global lv also)
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        res = []
        def subset(index):
            if index >= len(nums):
                result.append(list(res))
                return
            res.append(nums[index])
            subset(index + 1)
            res.remove(nums[index])
            subset(index + 1)
        subset(0)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.subsets([3,1,2]))