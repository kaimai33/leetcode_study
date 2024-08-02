class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [1] * len(nums)
        for i in range(1, len(lp)):
            lp[i] = nums[i-1] * lp[i-1]
        rp = [1] * len(nums)
        for i in range(len(rp) - 2, -1, -1):
            rp[i] = nums[i+1] * rp[i+1]
        ans = []
        for i in range(len(nums)):
            ans.append(lp[i] * rp[i])
        return ans
