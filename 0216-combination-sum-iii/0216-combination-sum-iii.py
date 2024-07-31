class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(k, n, curr_val, path):
            if k == 0 and n == 0:
                ans.append(path)
                return
            elif k == 0 or n < 0:
                return

            for i in range(curr_val, 10):
                dfs(k-1, n-i, i + 1, path + [i])
        
        dfs(k, n, 1, [])
        return ans