from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = lambda r: board[r]
        cols = lambda c: [r[c] for r in board]

        def flat_square(i):
            r = (i // 3) * 3
            c = (i % 3) * 3
            square = [b[c:c+3] for b in board[r:r+3]]
            return [val for row in square for val in row]

        def sudoku_counter(l):
            counter = Counter(l)
            if '.' in counter:
                del counter['.']
            return counter

        for i in range(9):
            counters = [sudoku_counter(l) for l in [rows(i), cols(i), flat_square(i)]]
            for counter in counters:
                mc = counter.most_common()
                if mc and mc[0][1] > 1:
                    return False
        return True
