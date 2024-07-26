class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            parts = word.split(separator)
            ans.extend(part for part in parts if part)
        return ans