class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def isPattern(subarray, pattern):
            for i in range(len(subarray) - 1):
                if pattern[i] == 1:
                    if subarray[i] < subarray[i+1]:
                        continue
                elif pattern[i] == 0:
                    if subarray[i] == subarray[i+1]:
                        continue
                elif pattern[i] == -1:
                    if subarray[i] > subarray[i+1]:
                        continue
                return False
            return True
        ans = 0
        length = len(pattern) + 1
        for i in range(len(nums) - len(pattern)):
            if isPattern(nums[i:i+length], pattern):
                ans += 1
        return ans
