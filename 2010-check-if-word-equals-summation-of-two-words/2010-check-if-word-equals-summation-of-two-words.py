class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        sum1 = ""
        sum2 = ""
        sum3 = ""
        for c in firstWord:
            sum1 += str(ord(c) - ord('a'))
        for c in secondWord:
            sum2 += str(ord(c) - ord('a'))
        for c in targetWord:
            sum3 += str(ord(c) - ord('a'))

        return int(sum1) + int(sum2) == int(sum3)