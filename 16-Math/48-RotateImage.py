# TRICKY

# Have left, right at the two ends of first row
# run a loop from left to right-1 TIMES (RIGHT-LEFT times) -> (n-1 times for a row)
# inside the loop. have top and bottom equal to left and right
# follow a clockwise rotation but in reverse (still clockwise but change the element in reverse)
# looking at the matrix, add i at the correct places
# This question is tricky, very easy to forget

# TC - n2, SC - 1

# Video -> https://neetcode.io/solutions/rotate-image
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix[0])-1

        while left < right:
            for i in range(right-left):
                top, bottom = left, right

                topLeft = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = topLeft
            
            left+=1
            right-=1





        