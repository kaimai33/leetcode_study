class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ok i read the answer, let's try recreate this from memory
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # if stack exists and the curr temp is greater than the latest in our stack
            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                ans[prev_idx] = i - prev_idx
            stack.append(i)
        
        return ans