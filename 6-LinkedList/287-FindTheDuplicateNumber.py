# Way - 0 (Brute Force)
# Way - 1 (Use hashMap or hashSet)
# Way - 2 (Modify the org array with negative nums since index and values <=n)
# Way - 3 (Floyd's cycle detection)

# https://neetcode.io/solutions/find-the-duplicate-number
# First find the intersection point in the cycle. then, distance from the intersection point and starting point of the list will always be same[THEORM]
# Have slow, fast pointers to do this.
# Floyd's cycle detection algo - SC = O(1) and n TC. Don't modify orginal array.
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Flyod's cycle detection
        # Step 1: Find out that it is a linked list cycle problem
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # Find starting point of the cycle
        p1 = 0
        while True:
            p1 = nums[p1]
            slow = nums[slow]

            if p1 == slow:
                break
        
        return p1
        

if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate([1,3,4,2,2]))
    print(s.findDuplicate([3,1,3,4,2]))
    print(s.findDuplicate([3,3,3,3,3]))
