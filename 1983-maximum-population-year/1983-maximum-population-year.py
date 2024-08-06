class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        hmap = {}
        max_freq = 0
        earliest = 2051
        for log in logs:
            for i in range(log[0], log[1]):
                hmap[i] = hmap.get(i, 0) + 1
                max_freq = max(max_freq, hmap[i])
        for key, value in hmap.items():
            if value == max_freq:
                earliest = min(earliest, key)
        return earliest

        