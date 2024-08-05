class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                prev_val = stack.pop()
                prev_prev_val = stack.pop()
                if token == '+':
                    stack.append(prev_prev_val + prev_val)
                elif token == '-':
                    stack.append(prev_prev_val - prev_val)
                elif token == '*':
                    stack.append(prev_prev_val * prev_val)
                elif token == '/':
                    stack.append( int(prev_prev_val / prev_val))
            else:
                stack.append(int(token))
        return stack[-1]