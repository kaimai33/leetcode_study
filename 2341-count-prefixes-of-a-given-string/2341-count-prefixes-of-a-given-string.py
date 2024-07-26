class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for word in words:
            if len(word) > len(s):
                continue
            if word == s[:len(word)]:
                ans += 1
        return ans