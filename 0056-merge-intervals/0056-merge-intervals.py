class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        ans = [intervals[0]]
        if len(intervals) == 1:
            return ans
        for i in range(1, len(intervals)):
            prev_end = ans[-1][1]
            if prev_end >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans