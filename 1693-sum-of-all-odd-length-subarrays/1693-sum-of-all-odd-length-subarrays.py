class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        for i in range(len(arr)):
            # subarray count of either in or out
            total_ways = (i + 1) * (n - i)
            odd_ways = (total_ways + 1) // 2
            ans += odd_ways * arr[i]
        return ans