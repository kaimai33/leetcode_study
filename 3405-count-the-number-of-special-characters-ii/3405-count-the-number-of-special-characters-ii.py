class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowerIdx = {}
        upperIdx = {}
        ans = 0
        for i, c in enumerate(word):
            if c.islower():
                lowerIdx[c] = i
            elif c.isupper():
                if c in upperIdx:
                    continue
                else:
                    upperIdx[c] = i
        for c, idx in lowerIdx.items():
            if c.upper() in upperIdx:
                upIdx = upperIdx[c.upper()]
                if idx < upIdx:
                    ans += 1
        return ans