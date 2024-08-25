class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for i in range(k):
            gifts.sort()
            val = gifts.pop()
            gifts.append(int(val ** 0.5))
        
        return sum(gifts)