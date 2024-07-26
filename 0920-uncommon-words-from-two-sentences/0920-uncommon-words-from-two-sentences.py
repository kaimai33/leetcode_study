class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        arr1 = s1.split()
        arr2 = s2.split()
        hmap = {}
        arr = []
        for w in arr1:
            hmap[w] = hmap.get(w, 0) + 1
        for w in arr2:
            hmap[w] = hmap.get(w, 0) + 1
        for key, value in hmap.items():
            if value == 1:
                arr.append(key)
        return arr
