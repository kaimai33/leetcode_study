class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        curr_xor = 0
        for num in nums:
            curr_xor ^= num

        difference = curr_xor ^ k

        bin_string = bin(difference)
        ans = 0
        for c in bin_string:
            if c == '1':
                ans += 1
        
        return ans
