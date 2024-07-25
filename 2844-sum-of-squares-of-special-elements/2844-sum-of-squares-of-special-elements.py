class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if len(nums) % (i + 1) == 0:
                ans += nums[i] ** 2
        return ans