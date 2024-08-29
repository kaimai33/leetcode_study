class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        arr = []
        sorted_map = dict(sorted(hmap.items(), key=lambda item: (item[1], -(item[0]))))
        for key, val in sorted_map.items():
            for i in range(val):
                arr.append(key)
        return arr