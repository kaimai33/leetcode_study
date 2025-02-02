class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        wrong = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                wrong += 1
        if nums[0] < nums[-1]:
            wrong += 1
        if wrong <= 1:
            return True
        return False