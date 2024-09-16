class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        posDiags = set() # r + c
        negDiags = set()

        ans = 0
        board = [['.'] * n for _ in range(n)]

        def backtrack(row):
            nonlocal ans
            # end case
            if row == n:
                ans += 1
                return

            for col in range(n):
                if col in cols or (row + col) in posDiags or (row - col) in negDiags: # occupied case, then we skip
                    continue
                # valid case
                cols.add(col)
                posDiags.add(row + col)
                negDiags.add(row - col)
                board[row][col] = 'Q'

                backtrack(row + 1)

                cols.remove(col)
                posDiags.remove(row + col)
                negDiags.remove(row - col)
                board[row][col] = '.'

        backtrack(0)
        return ans