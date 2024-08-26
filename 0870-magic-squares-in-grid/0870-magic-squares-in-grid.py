class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isValidSubsquare(r, c):
            sset = set([grid[r][c], grid[r][c+1], grid[r][c+2], grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2], grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]])
            if len(sset) != 9 or any(val < 1 or val > 9 for val in sset):
                return False
            
            r1 = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            r2 = grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2]
            r3 = grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2]
            c1 = grid[r][c] + grid[r+1][c] + grid[r+2][c]
            c2 = grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1]
            c3 = grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2]
            d1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]
            d2 = grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2]

            return r1 == r2 == r3 == c1 == c2 == c3 == d1 == d2 == 15
        

        # edge cases
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        ans = 0

        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if isValidSubsquare(i, j):
                    ans += 1
        
        return ans