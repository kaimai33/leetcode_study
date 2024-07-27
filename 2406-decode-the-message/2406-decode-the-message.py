class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        hmap = {}
        idx = 0

        for c in key:
            if c not in hmap and c != ' ':
                hmap[c] = chr(ord('a') + idx) # maps to a letter in the alphabet based on order found
                idx += 1
            if idx == 26:
                break

        ans = ""
        for c in message:
            if c == ' ':
                ans += ' '
            else:
                ans += hmap.get(c, c)
        return ans