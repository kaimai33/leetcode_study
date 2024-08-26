class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        aCount, bCount, cCount = 0, 0, 0
        ans = 0

        for i in range(len(s)):
            if s[i] == 'a':
                aCount += 1
            elif s[i] == 'b':
                bCount += 1
            elif s[i] == 'c':
                cCount += 1
            
            while aCount > 0 and bCount > 0 and cCount > 0:
                ans += len(s) - i # add all valid substrings past r
                if s[l] == 'a':
                    aCount -= 1
                elif s[l] == 'b':
                    bCount -= 1
                elif s[l] == 'c':
                    cCount -= 1
                l += 1 # we reduce the left side now
            
        return ans

