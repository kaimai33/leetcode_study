class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        ans = 0
        winners = set()
        for i in range(n):
            hmap = {}
            for j in range(len(pick)):
                if pick[j][0] == i: # if we find a tuple that matches the player val
                    hmap[pick[j][1]] = hmap.get(pick[j][1], 0) + 1
                    if hmap[pick[j][1]] > pick[j][0] and i not in winners:
                        winners.add(i)
                        ans += 1
                        continue 
        
        return ans