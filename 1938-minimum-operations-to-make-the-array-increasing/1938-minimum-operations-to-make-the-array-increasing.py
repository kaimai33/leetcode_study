class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                continue
            else:
                ans += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
        return ans