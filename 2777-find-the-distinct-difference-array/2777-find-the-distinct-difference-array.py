class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ldist = [0] * len(nums)
        rdist = [0] * len(nums)
        lset = set()
        rset = set()
        lidx = 0
        ridx = len(nums) - 1

        for i in range(len(nums)):
            lset.add(nums[i])
            ldist[lidx] = len(lset)
            lidx += 1
        for i in range(len(nums) - 1, -1, -1):
            rset.add(nums[i])
            rdist[ridx] = len(rset)
            ridx -= 1
        
        ans = [0] * len(nums)
        for i in range(len(nums)):
            l_dist_cnt = ldist[i]
            r_dist_cnt = rdist[i+1] if i+1 < len(nums) else 0
            ans[i] = l_dist_cnt - r_dist_cnt
        return ans