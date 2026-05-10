class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        # [[0, 1, 2], [3, 4, 5]]
        # 00  01  02  10  11 12
        # ROWS = 2, COLS = 3

        left, right = 0, ROWS * COLS - 1
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // COLS, mid % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid -1
        return False
