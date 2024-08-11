class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = [words[0]]
        curr = groups[0]
        for i in range(1, len(words)):
            if groups[i] != curr:
                ans.append(words[i])
                curr = groups[i]
        return ans