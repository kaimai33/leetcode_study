class Solution:
    def countElements(self, nums: List[int]) -> int:
        max_val = max(nums)
        min_val = min(nums)
        ans = 0
        for num in nums:
            if num != max_val and num != min_val:
                ans += 1
        return ans