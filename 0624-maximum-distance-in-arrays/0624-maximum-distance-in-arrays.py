class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = -1
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for array in arrays[1:]:
            ans = max(ans, max(abs(max_val - array[0]), abs(min_val - array[-1])))
            min_val = min(min_val, array[0])
            max_val = max(max_val, array[-1])

        return ans