class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(len(s) // 2):
            l, r = s[2*i], s[2*i+1]
            if l != r:
                ans += 1
        return ans

            
