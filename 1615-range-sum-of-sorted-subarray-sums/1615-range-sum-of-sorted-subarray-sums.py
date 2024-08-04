class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                arr.append(curr % (10 ** 9 + 7))
        arr.sort()
        return sum(arr[left-1:right]) % (10 ** 9 + 7)