class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:   
        """
        Thought process:
        1. convert to a base
        2. check palindrome
        """
        def to_base(n, base):
            if n == 0:
                return "0"
            digits = []
            while n:
                digits.append(str(n % base))
                n //= base
            return ''.join(digits[::-1])
        
        def isPalindrome(string):
            for i in range(len(string) // 2):
                if string[i] != string[-1 - i]:
                    return False
            return True
        
        for i in range(2, n - 1):
            if not isPalindrome(to_base(n, i)):
                return False
        return True
            