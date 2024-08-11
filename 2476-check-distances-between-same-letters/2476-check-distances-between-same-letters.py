class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # ans = [0] * 26
        # for i in range(len(s)):
        #     if ans[ord(s[i]) - ord('a')] == 0:
        #         ans[ord(s[i]) - ord('a')] -= i
        #     else:
        #         ans[ord(s[i]) - ord('a')] += i + 1
        # return ans == distance

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
