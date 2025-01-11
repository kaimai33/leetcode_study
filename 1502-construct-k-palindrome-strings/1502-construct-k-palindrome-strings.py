class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        hmap = {}
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
        odd_cnt = 0
        for key, val in hmap.items():
            if val % 2 == 1:
                odd_cnt += 1
        if odd_cnt > k:
            return False
        return True