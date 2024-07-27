class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        # initialize variables
        evensum = 0
        oddsum = 0
        for num in nums:
            if num % 2 == 0:
                evensum += num
            else:
                oddsum += num
        ans = []

        for query in queries:
            val = query[0]
            idx = query[1]
            prev_num = nums[idx]
            nums[idx] += val
            if prev_num % 2 == 0 and nums[idx] % 2 == 0:
                evensum += val
            elif prev_num % 2 == 1 and nums[idx] % 2 == 0:
                evensum += nums[idx]
            elif prev_num % 2 == 0 and nums[idx] % 2 == 1:
                evensum -= prev_num
            elif prev_num % 2 == 1 and nums[idx] % 2 == 1:
                evensum += 0
            ans.append(evensum)
        
        return ans

