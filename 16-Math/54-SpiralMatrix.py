# Similar to 48-Rotate Image(logic)
# have 4 loops - first row, last col, last row, first col inside main loop
# take the whole row or col
# left, right+1 -> first row
# top+1, bottom+1 -> last col
# right-1, left-1 -> last row
# bottom-1, top -> first col

# if left == right -> don't do first col or top == bottom -> don't do last row[THINK!!]
# Think for indexes
# Do a dry run

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1

        res = []

        while left <= right and top <= bottom:
            # First Row
            for i in range(left, right+1):
                res.append(matrix[left][i])
            
            # Last Col
            for i in range(top+1, bottom+1):
                res.append(matrix[i][right])
            
            # Last Row
            if top < bottom:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[bottom][i])
            
            # First Col
            if left < right:
                for i in range(bottom-1, top, -1):
                    res.append(matrix[i][left])
             
            left+=1
            right-=1
            top+=1
            bottom-=1
        
        return res





        