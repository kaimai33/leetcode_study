class Solution:
    def removeStars(self, s: str) -> str:
        """
        Thought Process:
        1. let's use a stack
        2. convert stack to string afterwards
        """
        ans = []
        for c in s:
            if c == '*':
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)