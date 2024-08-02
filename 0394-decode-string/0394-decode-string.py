class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_mult = 0
        curr_str = ""

        for c in s:
            if c.isdigit():
                curr_mult = curr_mult * 10 + int(c)
            elif c == '[':
                stack.append((curr_str, curr_mult))
                curr_str = ""
                curr_mult = 0
            elif c == ']':
                prev_str, prev_num = stack.pop()
                curr_str = prev_str + prev_num * curr_str
            else:
                curr_str += c
        return curr_str


            