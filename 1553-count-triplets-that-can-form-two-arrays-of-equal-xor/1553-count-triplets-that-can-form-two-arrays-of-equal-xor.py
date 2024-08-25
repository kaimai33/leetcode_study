class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [0]
        ans = 0

        for i in range(len(arr)):
            prefix_xor.append(arr[i] ^ prefix_xor[-1])

        for j in range(1, len(arr)):
            for i in range(0, j):
                xor_i = prefix_xor[j] ^ prefix_xor[i]
                for k in range(j, len(arr)):
                    xor_k = prefix_xor[j] ^ prefix_xor[k+1]
                    if xor_i == xor_k:
                        ans += 1
        
        return ans
                
