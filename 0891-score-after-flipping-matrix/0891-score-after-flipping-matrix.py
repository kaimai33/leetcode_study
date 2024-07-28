class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        """
        TP:
        1. flip all rows with a trailing zero
        2. get the max(ones, zeros) in each column afterwards
        3. convert
        """
        for i in range(len(grid)):
            if grid[i][0] == 1:
                continue
            for j in range(len(grid[0])):
                grid[i][j] = (grid[i][j] + 1) % 2
        ans = 0
        power = len(grid[0]) - 1
        for i in range(len(grid[0])):
            # we find the amt of ones and zeros in each col
            ones = 0
            zeros = 0
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    ones += 1
                else:
                    zeros += 1
            ans += max(ones, zeros) * (2 ** power)
            power -= 1
        
        return ans