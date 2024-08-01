class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        prefix_sum = sum(nums)

        for i in range(len(nums) - 1, -1, -1):
            prefix_sum -= nums[i]
            if prefix_sum > nums[i]:
                return prefix_sum + nums[i]

        return -1