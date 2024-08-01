class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def helper(r, c):
            # successful end case
            if r == len(grid):
                return c
            
            # unsuccessful end cases
            # stuck at left
            if grid[r][c] == -1:
                if c == 0:
                    return -1
                elif grid[r][c-1] == 1:
                    return -1
            
            # stuck at right
            if grid[r][c] == 1:
                if c == len(grid[0]) - 1:
                    return -1
                elif grid[r][c+1] == -1:
                    return -1
            
            # passes, then recurse to next square
            if grid[r][c] == 1:
                return helper(r+1,c+1)
            else:
                return helper(r+1,c-1)

        ans = []
        for i in range(len(grid[0])):
            ans.append(helper(0, i))
        return ans
