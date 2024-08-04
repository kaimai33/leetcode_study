class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hmap = {}
        hmap[(hours[0] % 24)] = 1
        ans = 0
        for i in range(1, len(hours)):
            curr = (hours[i] % 24)
            comp = (24 - curr) % 24 # handles curr == 0, because hr 24 == hr 0
            if comp in hmap:
                ans += hmap[comp]
            hmap[curr] = hmap.get(curr, 0) + 1
        
        return ans