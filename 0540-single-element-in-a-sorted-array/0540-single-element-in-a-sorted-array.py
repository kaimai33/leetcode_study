class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Thought process:
        1. binary search.
        2. array is odd length
        3. if the dupe is neither on left or right side, then return mid
        4. if dupe is on right, then recurse on left
        5. if dupe is on left, then recurse on right
        """

        def binSearch(l, r):
            if l == r:
                return nums[l]
            
            m = (l + r) // 2
            if m % 2 == 1:
                m -= 1 # m has to be even, bruh why. This puts us on the left side of each dupe?


            if nums[m] == nums[m+1]:
                return binSearch(m + 2, r)
            elif nums[m] == nums[m-1]:
                return binSearch(l, m)
            else:
                return nums[m]
        return binSearch(0, len(nums) - 1)