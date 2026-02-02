# https://neetcode.io/solutions/permutations
# We can solve it with single recursion, no branching required(no multiple recursions required)
# for [1,2,3]
# we keep on removing the first element, recursion till the base case then return []
# insert first element at every i for every r in result and return that up in the recursion
# In each recursion step, you take existing list and create a new list and return
# Refer 46-all_permutations jpg for the recursion stack

# Copy is required because of the loop

# TC = n! * n2, SC = n!(Copy space)
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if nums == []:
            return [[]]
        
        perm = self.permute(nums[1:])
        res = []
        for r in perm:
            for i in range(len(r)+1):
                r_copy = r.copy() # make a copy
                r_copy.insert(i, nums[0])
                res.append(r_copy)
        return res

# Call the test function
if __name__ == "__main__":
    s = Solution()
    print(s.permute([1,2,3]))