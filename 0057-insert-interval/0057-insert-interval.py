class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Thought process:
        3 steps: 
            1. add all intervals to the left
            2. find the insert location, may have to merge
            3. add remaining intervals

        """
        n = len(intervals)
        ans = []
        i = 0

        # step 1
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1
        
        # step 2 - we found a case such that the interval start is >= the start of newInterval start
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        ans.append(newInterval)

        while i < n:
            ans.append(intervals[i])
            i += 1
        
        return ans
