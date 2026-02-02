# Space - O(m+n)
# have two arrays for row and col(set or index arr)
# mark which row or col has matrix[row][col] == 0 then, mark that rows or cols -> 0

# Space - O(1) [TRICKY]
# Use the input arr space as row, col arr
# first row -> have it for cols zero
# first col -> have it for rows zero

# but it will overlap at (0,0)
# so, have a bool (zeroRow)

# When setting zeros
# do 1,Row and 1,col first (make them zeros first)
# then do (0,0) for first col
# because 0 col will change first col also(we don't want that)
# IN LAST do zeroRow
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRow = False

        ROW = len(matrix)
        COL = len(matrix[0])

        
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        zeroRow = True
        
        for i in range(1, ROW):
            for j in range(1, COL):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for i in range(ROW):
                matrix[i][0] = 0
        
        if zeroRow:
            for j in range(COL):
                matrix[0][j] = 0