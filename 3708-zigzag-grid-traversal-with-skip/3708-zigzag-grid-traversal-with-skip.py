class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for r in range(len(grid)):
            curr = []
            if r % 2 == 0:
                for c in range(0, len(grid[0]), 2):
                    curr.append(grid[r][c])
                ans += curr
            else:
                for c in range(1, len(grid[0]), 2):
                    curr.append(grid[r][c])
                ans += curr[::-1]
            
        return ans


