class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans_set = set(nums[0])
        for i in range(1, len(nums)):
            ans_set = ans_set & set(nums[i])
        return sorted(list(ans_set))