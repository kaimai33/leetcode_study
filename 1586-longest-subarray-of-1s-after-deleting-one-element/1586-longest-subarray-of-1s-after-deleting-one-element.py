class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt0 = 0
        l = 0
        for r, num in enumerate(nums):
            if num == 0:
                cnt0 += 1
            while cnt0 == 2:
                if nums[l] == 0:
                    cnt0 -= 1
                l += 1
            ans = max(ans, r - l)
        return ans
                