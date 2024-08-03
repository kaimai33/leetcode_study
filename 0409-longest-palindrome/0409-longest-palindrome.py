class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        ddict = []
        for i in range(len(s)):
            if s[i] in ddict:
                pairs += 1
                ddict.remove(s[i])
            else:
                ddict.append(s[i])
        if len(ddict) >= 1:
            return pairs*2 + 1
        return pairs*2
