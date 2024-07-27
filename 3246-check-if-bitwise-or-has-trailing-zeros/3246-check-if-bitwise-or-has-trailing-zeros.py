class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        evennums = 0
        for num in nums:
            if num % 2 == 0:
                evennums += 1
            if evennums == 2:
                return True
        return False