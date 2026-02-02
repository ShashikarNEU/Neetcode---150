# TRICKY QUESTION
# find lowest and highest and do binary serach wity mid
# see how elements in matrix are within mid. if count > mid then, high = mid-1 else low = mid + 1
# while searching for elements <= mid in matrix use sorted arr trick for n2(two for loops). 
# Use sorted arr trick in code(in comments)!!

# for answer, just return low. You can only find this through dry runs.

# TC = log(max-min)*n (sorted search using mid in the matrix)

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        low = matrix[0][0]
        high = matrix[n-1][m-1]

        while low <= high:
            mid = (low+high)//2

            count = 0
            # for i in range(n):
            #     for j in range(m):
            #         if matrix[i][j] <= mid:
            #             count += 1

            # Sorted Search in the matrix
            # This is the heart of the question
            # start from the top-right and see how much element are there and move left or down[THINK!!]
            row, col = 0, m-1
            # row can be goes to n-1(< n) and col can go to 0(>= 0)
            while row < n and col >= 0:
                if matrix[row][col] <= mid:
                    # Col starts from 0
                    count += (col+1)
                    row += 1
                else:
                    col-=1
            
            if count >= k:
                high = mid - 1
            elif count < k:
                low = mid + 1
        
        # >= is in count >= k not count < k, if count >= k then, low will be mid-1(closer to k) [JUST REMEMBER THIS!!]
        return low
            
        
            