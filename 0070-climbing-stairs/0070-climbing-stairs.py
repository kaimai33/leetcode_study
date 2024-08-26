class Solution:
    def climbStairs(self, n: int) -> int:
        n1, n2, n3 = 1, 2, 0
        if n == 1:
            return n1
        elif n == 2:
            return n2
        for i in range(2, n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3
