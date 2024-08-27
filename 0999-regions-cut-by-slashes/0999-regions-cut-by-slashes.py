class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def bfs(r, c):
            new_grid[r][c] = 1
            if r > 0:
                if new_grid[r-1][c] == 0:
                    bfs(r-1,c)
            if r < len(new_grid) - 1:
                if new_grid[r+1][c] == 0:
                    bfs(r+1,c)
            if c > 0:
                if new_grid[r][c-1] == 0:
                    bfs(r,c-1)
            if c < len(new_grid[0]) - 1:
                if new_grid[r][c+1] == 0:
                    bfs(r,c+1)

        new_grid = [[0] * len(grid[0]) * 3 for _ in range(len(grid) * 3)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '/':
                    new_grid[3*i][3*j+2] = 1
                    new_grid[3*i+1][3*j+1] = 1
                    new_grid[3*i+2][3*j] = 1
                elif grid[i][j] == '\\':
                    new_grid[3*i][3*j] = 1
                    new_grid[3*i+1][3*j+1] = 1
                    new_grid[3*i+2][3*j+2] = 1
                else:
                    continue
        ans = 0
        for i in range(len(new_grid)):
            for j in range(len(new_grid[0])):
                if new_grid[i][j] == 0:
                    bfs(i, j)
                    ans += 1
        
        return ans