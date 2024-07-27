class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = set()
        for i in range(len(nums) // 2):
            averages.add((nums[i] + nums[-i-1]) / 2)
        return len(averages)