class Solution:
    # def vaild(self, )

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        grid = defaultdict(set)
        # key = set, value = 
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if (
                    board[i][j] in col[j]
                    or board[i][j] in row[i]
                    or board[i][j] in grid[(i // 3, j // 3)]
                ):
                    return False
                col[j].add(board[i][j])
                row[i].add(board[i][j])
                grid[(i // 3, j // 3)].add(board[i][j])
        return True

        # (0, 0) (0, 1) ... (0, 9)
        # (0, 0) (1, 0) ... (9, 0)