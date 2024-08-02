class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[0:k])
        ans = curr_sum / k
        for i in range(1, len(nums) - k + 1): # remember the +1 next time!
            curr_sum -= nums[i-1]
            curr_sum += nums[i + k - 1] # remember the -1 next time!
            ans=max(ans, curr_sum/k)
        return ans