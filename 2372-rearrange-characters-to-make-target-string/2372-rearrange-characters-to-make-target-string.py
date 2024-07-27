class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        t_hmap = {}
        s_hmap = {}
        for c in target:
            t_hmap[c] = t_hmap.get(c, 0) + 1
        for c in s:
            s_hmap[c] = s_hmap.get(c, 0) + 1
        ans = float('inf')
        for key, value in t_hmap.items():
            if key not in s_hmap:
                return 0
            else:
                ans = min(ans, s_hmap[key] // t_hmap[key])
        return ans