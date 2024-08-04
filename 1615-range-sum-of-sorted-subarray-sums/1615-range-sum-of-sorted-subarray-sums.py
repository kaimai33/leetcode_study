class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        # step 1 - generate all subarray sums
        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                arr.append(curr_sum % (10 ** 9 + 7))
        arr.sort()
        return sum(arr[left-1:right]) % (10 ** 9 + 7)