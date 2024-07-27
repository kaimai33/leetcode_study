class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # xor the two values, and count the ones
        return bin(start ^ goal).count('1')