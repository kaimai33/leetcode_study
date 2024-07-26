class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        hmap = {}
        for num in arr:
            hmap[num] = hmap.get(num, 0) + 1
        for key, value in hmap.items():
            if key == value and key > ans:
                ans = key
        return ans