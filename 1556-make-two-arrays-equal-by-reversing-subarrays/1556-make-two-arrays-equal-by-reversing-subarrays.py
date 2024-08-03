class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hmap1, hmap2 = {}, {}
        for i in range(len(target)):
            hmap1[target[i]] = hmap1.get(target[i], 0) + 1
            hmap2[arr[i]] = hmap2.get(arr[i], 0) + 1
        return hmap1 == hmap2