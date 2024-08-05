class Solution:
    def removeDuplicates(self, s: str) -> str:
        # stack problem
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
                continue
            if c == stack[-1]:
                stack.pop()
                continue
            stack.append(c)
        return ''.join(stack)
            