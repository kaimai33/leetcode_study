class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5
        arr = [0] * (n+1)
        arr[1] = 1
        arr[2] = 2
        arr[3] = 5
        
        for i in range(4, len(arr)):
            arr[i] = (2*arr[i-1] + arr[i-3]) % (10 ** 9 + 7)
        return arr[n]