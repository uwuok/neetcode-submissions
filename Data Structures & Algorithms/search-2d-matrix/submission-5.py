class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COLS = len(matrix[0])
        ROWS = len(matrix)
        
        top, bot = 0, ROWS - 1
        row = -1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] <= target <= matrix[mid][COLS - 1]:
                row = mid
                break 
            elif matrix[mid][0] < target:
                top = mid + 1
            elif matrix[mid][COLS - 1] > target:
                bot = mid - 1

        if row == -1:
            return False
        
        cl, cr = 0, COLS - 1
        while cl <= cr:
            mid = (cl + cr) // 2
            if matrix[row][mid] < target:
                cl = mid + 1
            elif matrix[row][mid] > target:
                cr = mid - 1
            else:
                return True
        return False 
            