from collections import Counter

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = lambda r: board[i]
        cols = lambda c: [r[c] for r in board]
        def squares(s: int) -> list[list[str]]:
            r = (s // 3) * 3
            c = (s % 3) * 3
            return [b[c:c+3] for b in board[r:r+3]]
        flat_square = lambda s: [v for l in squares(s) for v in l]
        def sudoku_counter(l: list[str]) -> Counter:
            counter = Counter(l)
            if '.' in counter:
                del counter['.']
            return counter

        for i in range(9):
            row = rows(i)
            col = cols(i)
            sq = flat_square(i)

            # print(i, col)


            # row_counter = sudoku_counter(row)
            # col_counter = sudoku_counter(col)
            # sq_counter = sudoku_counter(sq)
            
            # rmc = row_counter.most_common()
            # if rmc and rmc[0][1] > 1:
            #     return False
            
            # cmc = row_counter.most_common()
            # if cmc and cmc[0][1] > 1:
            #     return False
            
            # smc = row_counter.most_common()
            # if smc and smc[0][1] > 1:
            #     return False


            counters = [sudoku_counter(l) for l in [row,col,sq]]
            print(i, counters)
            for counter in counters:
                mc = counter.most_common()
                # print(mc)
                if mc and mc[0][1] > 1:
                    print(mc)
                    return False
        return True
