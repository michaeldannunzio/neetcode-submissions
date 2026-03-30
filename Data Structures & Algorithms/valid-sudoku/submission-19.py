from collections import Counter

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = lambda r: board[i]
        cols = lambda c: [r[c] for r in board]

        def flat_square(i: int) -> list[list[str]]:
            r = (i // 3) * 3
            c = (i % 3) * 3
            s = [b[c:c+3] for b in board[r:r+3]]
            return [v for l in s for v in l]

        def sudoku_counter(l: list[str]) -> Counter:
            counter = Counter(l)
            if '.' in counter:
                del counter['.']
            return counter

        for i in range(9):
            counters = [sudoku_counter(l) for l in [rows(i),cols(i),flat_square(i)]]
            for counter in counters:
                mc = counter.most_common()
                if mc and mc[0][1] > 1:
                    return False
        return True
