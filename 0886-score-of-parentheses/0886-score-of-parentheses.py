class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # ans = 0
        # multiplier = 1
        # stack = []
        # for c in s:
        #     if c == '(':
        #         multiplier = 1
        #         stack.append('(')
        #     elif c == ')':
        #         while stack and stack[-1] == '(':
        #             stack.pop()
        #             ans += multiplier
        #             multiplier += 1
        # return ans
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(2 * val, 1)
        return stack.pop()
