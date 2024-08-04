class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        left_min = [0] * len(nums)
        curr_left_min = nums[0]
        right_min = [0] * len(nums)
        curr_right_min = nums[-1]

        for i in range(1, len(left_min)):
            left_min[i] = curr_left_min
            curr_left_min = min(curr_left_min, nums[i])

        for i in range(len(right_min) - 2, -1, -1):
            right_min[i] = curr_right_min
            curr_right_min = min(curr_right_min, nums[i])

        ans = float('inf')
        for i in range(1, len(nums) - 1):
            if nums[i] > left_min[i] and nums[i] > right_min[i]:
                ans = min(ans, nums[i] + left_min[i] + right_min[i])
        return ans if ans != float('inf') else -1
