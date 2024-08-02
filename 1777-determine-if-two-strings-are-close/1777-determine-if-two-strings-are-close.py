class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        hmap1 = {}
        hmap2 = {}
        for c in word1:
            hmap1[c] = hmap1.get(c, 0) + 1
        for c in word2:
            hmap2[c] = hmap2.get(c, 0) + 1
        arr1key = []
        arr1val = []
        arr2key = []
        arr2val = []
        for key, val in hmap1.items():
            arr1key.append(ord(key))
            arr1val.append(val)
        for key, val in hmap2.items():
            arr2key.append(ord(key))
            arr2val.append(val)
        arr1key.sort()
        arr1val.sort()
        arr2val.sort()
        arr2key.sort()
        
        return arr1key == arr2key and arr1val == arr2val