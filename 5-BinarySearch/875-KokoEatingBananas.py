# piles=[3,6,7,11], h=8
import math
# https://neetcode.io/solutions/koko-eating-bananas
# LOGIC (Do a dry run and understand logic)
# Take max of piles and see that summation(piles[i]/k) == h, so from 1 to max_piles
# we need to find the min num from there. apply binary search and use this codn to compare with h(summation(piles[i]/k))
# if h > codn, middle should be less. high = middle - 1 and record res = middle and vice versa. when we decrease middle, record it in res
# and return res after binary search is over
# we are trying to find min k and not when target_h == h(Remember it!!)[we record middle in res, when we are decreasing it]

# TC = O(m*logn)

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_pile = max(piles)

        low = 1
        high = max_pile
        res = 0

        while low <= high:
            middle = (low+high)//2

            target_h = 0
            for i in range(len(piles)):
                target_h += math.ceil(piles[i]/middle)
            
            if target_h <= h:
                res = middle # record min
                high = middle - 1
            elif target_h > h:
                low = middle + 1

        return res
                
if __name__ == "__main__":
    s = Solution()
    print(s.minEatingSpeed([3,6,7,11],8))
    print(s.minEatingSpeed([312884470],312884469))
