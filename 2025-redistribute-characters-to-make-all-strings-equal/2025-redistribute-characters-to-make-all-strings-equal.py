class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hmap = {}
        for word in words:
            for c in word:
                hmap[c] = hmap.get(c, 0) + 1
        
        for key, val in hmap.items():
            if val % len(words) != 0:
                return False
        
        return True