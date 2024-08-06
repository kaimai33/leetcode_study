class Solution:
    def minimumPushes(self, word: str) -> int:
        hmap = {}
        ans = 0
        for c in word:
            hmap[c] = hmap.get(c, 0) + 1
        sorted_freq = dict(sorted(hmap.items(), key = lambda i: i[1], reverse=True))
        count = []
        for i in range(len(sorted_freq)):
            if i < 8:
                count.append(1)
            elif i < 16:
                count.append(2)
            elif i < 24:
                count.append(3)
            elif i < 32:
                count.append(4)
        for i, (char, freq) in enumerate(sorted_freq.items()):
            ans += freq * count[i]
        return ans
