class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            s = set()
            for j in range(i, len(nums)):
                s.add(nums[j])
                ans += len(s) * len(s)
        return ans
