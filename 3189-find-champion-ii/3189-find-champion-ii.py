class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        winners = set()
        losers = set()
        for i in range(n):
            winners.add(i)
        for edge in edges:
            winner = edge[0]
            loser = edge[1]
            if winner not in losers:
                winners.add(winner)
            losers.add(loser)
            if loser in winners:
                winners.remove(loser)
        if len(winners) == 1:
            return list(winners)[0]
        else:
            return -1