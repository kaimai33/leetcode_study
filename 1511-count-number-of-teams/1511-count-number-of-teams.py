class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans = 0

        for i in range(1, len(rating) - 1):
            lLess, lMore, rLess, rMore = 0, 0, 0, 0
            for j in range(i - 1, -1, -1):
                if rating[j] < rating[i]:
                    lLess += 1
                elif rating[j] > rating[i]:
                    lMore += 1
            for j in range(i + 1, len(rating)):
                if rating[j] < rating[i]:
                    rLess += 1
                elif rating[j] > rating[i]:
                    rMore += 1
            ans += lLess * rMore + lMore * rLess
        
        return ans