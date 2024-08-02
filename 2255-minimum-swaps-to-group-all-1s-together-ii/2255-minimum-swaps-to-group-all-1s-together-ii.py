class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        new_arr = nums + nums
        curr_ones = sum(new_arr[0:ones])
        ans = ones - curr_ones
        for i in range(len(new_arr) - ones):
            if i < len(new_arr) - ones - 1:
                prev = new_arr[i]
                nxt = new_arr[i + ones]
                if prev == 1:
                    curr_ones -= 1
                if nxt == 1:
                    curr_ones += 1
                ans = min(ans, ones - curr_ones)
            
        return ans
