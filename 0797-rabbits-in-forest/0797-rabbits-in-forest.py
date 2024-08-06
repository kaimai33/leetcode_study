class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hmap = {}
        ans = 0
        for i in range(len(answers)):
            hmap[answers[i]+1] = hmap.get(answers[i]+1, 0) + 1
            if hmap[answers[i]+1] == answers[i] + 1:
                ans += answers[i] + 1
                del hmap[answers[i]+1]
        for key, value in hmap.items():
            ans += key
        return ans