class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        # 找行
        left_row, right_row = 0, m - 1
        while left_row <= right_row:
            mid_row = (left_row + right_row) // 2
            if matrix[mid_row][0] == target:
                return True
            elif matrix[mid_row][0] < target:
                left_row = mid_row + 1
            else:
                right_row = mid_row - 1
        
        row = right_row  # 這是 target 可能所在的行
        if row < 0:  # target 比第一行還小
            return False
        
        # 找列
        left_col, right_col = 0, n - 1
        while left_col <= right_col:
            mid_col = (left_col + right_col) // 2
            if matrix[row][mid_col] == target:
                return True
            elif matrix[row][mid_col] < target:
                left_col = mid_col + 1
            else:
                right_col = mid_col - 1
        
        return False
