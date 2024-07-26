class Solution:
    def totalMoney(self, n: int) -> int:
        prev_mon = 1
        ans = 0
        
        for i in range(n):
            week = i // 7
            day = i % 7
            ans += (prev_mon + week + day)
        
        return ans