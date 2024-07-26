class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        ans = 0
        for i in range(max_val, max_val + k):
            ans += i
        return ans