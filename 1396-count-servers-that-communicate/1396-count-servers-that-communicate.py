class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = {}
        cols = {}
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows[i] = rows.get(i, 0) + 1
                    cols[j] = cols.get(j, 0) + 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if rows[i] > 1 or cols[j] > 1:
                        ans += 1
        return ans
