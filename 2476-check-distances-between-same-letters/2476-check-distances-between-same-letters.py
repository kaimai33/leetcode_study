class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hmap = {}
        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = i
            else:
                prev_idx = hmap[s[i]]
                dist_idx = ord(s[i]) - ord('a')
                if i - prev_idx - 1 != distance[dist_idx]:
                    return False
        return True
