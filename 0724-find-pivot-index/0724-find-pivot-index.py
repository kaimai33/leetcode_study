class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        lsum = 0
        for i in range(len(nums)):
            total -= nums[i]
            if total == lsum:
                return i
            lsum += nums[i]
        return -1