class Solution:
    def countAsterisks(self, s: str) -> int:
        count = True
        ans = 0
        for c in s:
            if c == '|':
                count = not count
            if count and c == '*':
                ans += 1
        return ans