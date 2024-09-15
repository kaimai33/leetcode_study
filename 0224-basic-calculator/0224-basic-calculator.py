class Solution:
    def calculate(self, s: str) -> int:
        curr = 0
        res = 0
        sign = 1
        stack = []

        for c in s:
            if c.isdigit():
                curr *= 10
                curr += int(c)
            elif c in ['+', '-']:
                res += curr * sign
                if c == '+':
                    sign = 1
                else:
                    sign = -1
                curr = 0
            elif c == '(':
                # cache the current val and sign
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ')':
                res += sign * curr
                # find last vals - sign, then prev val
                res *= stack.pop()
                res += stack.pop()
                curr = 0

        return res + curr * sign