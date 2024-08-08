class Solution:
    def countEven(self, num: int) -> int:
        def isEvenDigitSum(n):
            ssum = 0
            string = str(n)
            for i in range(len(string)):
                ssum += int(string[i])
            return ssum % 2 == 0
        ans = 0
        for i in range(1, num + 1):
            if isEvenDigitSum(i):
                ans += 1
        return ans