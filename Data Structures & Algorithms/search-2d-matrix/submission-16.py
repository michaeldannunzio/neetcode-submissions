class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])
        l, r = 0, n_rows * n_cols - 1
        while l <= r:
            i = ((r - l) // 2) + l
            row_i = i // (n_rows + 1)
            col_i = i % (n_cols + 1)
            # row_i = 2
            # print(f'l={l}  r={r}  i={i}  row_i={row_i}  col_i={col_i}')
            v = matrix[row_i][col_i]
            if v > target:
                r = i - 1
            elif v < target:
                l = i + 1
            else:
                return True
        return False
