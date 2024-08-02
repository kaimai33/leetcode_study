class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(r, c, visited):
            # invalid case
            if (min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
            ans = grid[r][c]
            neighbors = [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]
            for r2, c2 in neighbors:
                ans = max(ans, grid[r][c] + dfs(r2,c2,visited))
            visited.remove((r, c))
            return ans

        ROWS, COLS = len(grid), len(grid[0])

        ans = 0
        for r in range(ROWS):
            for c in range(COLS):
                ans = max(ans, dfs(r, c, set()))
        return ans