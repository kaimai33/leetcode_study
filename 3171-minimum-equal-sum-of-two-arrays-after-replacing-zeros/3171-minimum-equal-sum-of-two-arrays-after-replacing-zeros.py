class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        a1Zeros = 0
        a1Sum = sum(nums1)
        a2Zeros = 0
        a2Sum = sum(nums2)
        for num in nums1:
            if num == 0:
                a1Zeros += 1
        for num in nums2:
            if num == 0:
                a2Zeros += 1

        a1Sum += a1Zeros
        a2Sum += a2Zeros
        if a1Sum < a2Sum and a1Zeros == 0:
            return -1
        elif a2Sum < a1Sum and a2Zeros == 0:
            return -1
        return max(a1Sum, a2Sum)
