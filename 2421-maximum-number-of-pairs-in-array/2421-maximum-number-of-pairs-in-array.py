class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        ans1 = 0
        ans2 = 0
        for key, value in hmap.items():
            ans1 += value // 2
            ans2 += value % 2
        return [ans1, ans2]