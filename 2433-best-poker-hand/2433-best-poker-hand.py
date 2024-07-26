class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        # check for flush
        if ''.join(suits) == suits[0]*5:
            return "Flush"
        # check for 3 of a kind
        cards = set(ranks)
        hmap = {}
        for c in ranks:
            hmap[c] = hmap.get(c, 0) + 1
            if hmap[c] == 3:
                return "Three of a Kind"
        if len(cards) <= 4:
            return "Pair"
        return "High Card"