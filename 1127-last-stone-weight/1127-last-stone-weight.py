class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # python does not support max-heap, we have to use a min-heap instead
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones) # least (greatest) val
            x = heapq.heappop(stones) # second least val
            if x > y:
                heapq.heappush(stones, y - x)
        if len(stones) == 0:
            return 0
        else:
            return abs(stones[0])
            