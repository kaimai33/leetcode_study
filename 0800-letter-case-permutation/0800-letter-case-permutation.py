class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def rec(string, idx):
            if idx == len(s):
                ans.append(string)
                return
            if s[idx].isdigit():
                rec(string + s[idx], idx + 1)
            else:
                rec(string + s[idx].upper(), idx + 1)
                rec(string + s[idx].lower(), idx + 1)
        rec("", 0)
        return ans
