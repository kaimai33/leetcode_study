class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        string = str(bin(n))[2:]
        print(string)
        even, odd = 0, 0
        idx = 0
        for i in range(len(string) - 1, -1, -1):
            if idx % 2 == 0 and string[i] == '1':
                even += 1
            elif idx % 2 == 1 and string[i] == '1':
                odd += 1
            idx += 1        
        return [even, odd]