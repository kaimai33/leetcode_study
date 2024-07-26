class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        new_arr = [nums[0]]
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                new_arr.append(nums[i])
        if len(new_arr) < 3:
            return 0
        for i in range(1, len(new_arr) - 1):
            if (new_arr[i] < new_arr[i-1] and new_arr[i] < new_arr[i+1]) or (new_arr[i] > new_arr[i-1] and new_arr[i] > new_arr[i+1]):
                ans += 1
        return ans

