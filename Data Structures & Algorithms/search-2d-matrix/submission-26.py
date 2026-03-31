class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])
        l, r = 0, n_rows * n_cols - 1
        while l <= r:
            i = ((r - l) // 2) + l
            row_i, col_i = i // n_cols, i % n_cols
            v = matrix[row_i][col_i]
            if v > target:
                r = i - 1
            elif v < target:
                l = i + 1
            else:
                return True
        return False
