class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for idx, c in enumerate(s):
            print(ord(c) - 96)
            ans += (idx + 1) * (27 - (ord(c) - 96))
        return ans
        