class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """ 
        TP:
        bin search, why is this a medium problem lol??
        """
        def binSearch(l, r):
            while l < r:
                m = (l + r) // 2
                if arr[m] < arr[m + 1]:
                    l = m + 1
                else:
                    r = m
            return l
        return binSearch(0, len(arr) - 1)