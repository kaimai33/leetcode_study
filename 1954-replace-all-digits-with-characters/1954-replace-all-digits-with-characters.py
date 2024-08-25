class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if s[i].isdigit():
                prev_char = ans[-1]
                ans += chr(ord(prev_char) + int(s[i]))
            else:
                ans += s[i]
        
        return ans