# [INFAMOUS HARD PROBELM!!]
# https://neetcode.io/solutions/median-of-two-sorted-arrays
# Watch the video and do a dry run first
# We do binary serach on the smaller array and find middle. We need to compare Aleft,Bleft with Bright,Aright. left, right means
# left half and right half of the merged sorted array. To find the middle of the larger array, do half total length - middle of smaller array, then find Aleft,Bleft and Bright,Aright from there. handle out of bounds indexes for A, B. Now, compare A,B. 
# case 1: if Aleft <= Bright and Bleft <= Aright --> partition is correct then for odd case, min(right of A and B) -> ans
# if even -> (max(Aleft,Bleft)+min(Bright,Aright))/2 [Think about this from merged perpsective]

# Aleft > Bright: -> Aleft should be small so, do high = middle_A - 1
# Bleft > Aright: -> A left should be big then Bleft will be small so do, low = middle_A + 1
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A = nums1
        B = nums2

        # We just need to do binary search on the smaller one
        if len(B) < len(A):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total//2
       

        low = 0
        high = len(A)-1
        while True:
            middle_A = (low+high)//2
            # we put -2 because half and middle_A is not indexes(starts from 0)[IMP]
            middle_B = half - middle_A - 2

            Aleft = A[middle_A] if middle_A >= 0 else float('-inf')
            Aright = A[middle_A+1] if middle_A+1 < len(A) else float('inf')
            Bleft = B[middle_B] if middle_B >= 0 else float('-inf')
            Bright = B[middle_B+1] if middle_B+1 < len(B) else float('inf')

            # Parition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Total length is odd case
                if total % 2 != 0:
                    return min(Aright, Bright)
                
                # Even case
                return (max(Aleft, Bleft) + min(Bright, Aright))/2
            elif Aleft > Bright:
                high = middle_A - 1
            # Bleft > Aright
            else:
                low = middle_A + 1

if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,3], [2]))
    print(s.findMedianSortedArrays([1,2], [3,4]))
                
                
            
            