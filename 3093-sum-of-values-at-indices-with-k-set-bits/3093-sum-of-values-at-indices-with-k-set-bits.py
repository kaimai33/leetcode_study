class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, num in enumerate(nums):
            string = bin(i)
            cnt = 0
            for c in string:
                if c == '1':
                    cnt += 1
            if cnt == k:
                ans += num
        return ans 