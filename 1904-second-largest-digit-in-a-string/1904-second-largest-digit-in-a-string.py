class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for c in s:
            if c.isdigit():
                digits.add(int(c))
        if len(digits) <= 1:
            return -1
        arr = sorted(list(digits))
        return arr[-2]