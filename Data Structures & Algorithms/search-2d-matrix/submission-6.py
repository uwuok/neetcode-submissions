class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        row = -1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] < target:
                top = mid + 1
            elif matrix[mid][-1] > target:
                bot = mid - 1

        if row == -1:
            return False

        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] > target:
                right = mid - 1
        return False