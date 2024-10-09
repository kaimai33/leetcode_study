class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        chars = list(s)
        openCount = 0
        closedCount = 0
        for idx, c in enumerate(chars):
            if c == '(':
                openCount += 1
            elif c == ')':
                if openCount == 0:
                    ans += 1
                else:
                    openCount -= 1
        return ans + openCount