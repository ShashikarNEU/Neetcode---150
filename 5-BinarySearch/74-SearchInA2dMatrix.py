# One soln is to binary on each row (TC = no of rows * log(cols)=nlogm)
# But we can do log(m) + log(n) soln
# First we find the row via binary search, codn -> compare target with matrix[row][-1] and matrix[row][0], 
# it will be greater or lesser. If it's in between then thats ur result row. Then result row, apply normal binary search
# to the answer

# Edge cases: there can be matrix[middle][0] == target or matrix[middle][-1] == target, instead of writing long lines, just use else
# After finding result row(row where the ans is), break the loop
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])
        # Find the rows first
        low = 0
        high = ROW-1
        result_row = -1

        while low <= high:
            middle = (low+high)//2

            if matrix[middle][0] > target and matrix[middle][-1] > target:
                high = middle - 1
            elif matrix[middle][0] < target and matrix[middle][-1] < target:
                low = middle + 1
            else:
                result_row = middle
                break
            # elif matrix[middle][0] < target and matrix[middle][-1] > target:
            #     result_row = middle
        
        if result_row == -1:
            return False
        # In that row, find that col of the target
        low = 0
        high = COL-1
        while low <= high:
            middle = (low+high)//2

            if matrix[result_row][middle] > target:
                high = middle - 1
            elif matrix[result_row][middle] < target:
                low = middle + 1
            else:
                return True
            # elif matrix[result_row][middle] == target:
            #     return True
        
        return False

# Other Attempt
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        start = 0
        end = len(matrix)-1
        col_len = len(matrix[0])-1
        res_row = -1

        while start <= end:
            middle = (start+end) // 2

            if matrix[middle][0] > target and matrix[middle][col_len] > target:
                end = middle - 1
            elif matrix[middle][0] < target and matrix[middle][col_len] < target:
                start = middle + 1
            else:
                res_row = middle
                break
        
        if res_row == -1:
            return False
        
        res_start = 0
        res_end = col_len
        while res_start <= res_end:
            middle = (res_start+res_end)//2
            if matrix[res_row][middle] == target:
                return True
            elif matrix[res_row][middle] > target:
                res_end = middle - 1
            elif matrix[res_row][middle] < target:
                res_start = middle + 1

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))