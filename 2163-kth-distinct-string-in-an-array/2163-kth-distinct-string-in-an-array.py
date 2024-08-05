class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hmap = {}
        for string in arr:
            hmap[string] = hmap.get(string, 0) + 1
        new_arr = []
        for key, val in hmap.items():
            if val == 1:
                new_arr.append(key)
        if k > len(new_arr):
            return ""
        else:
            return new_arr[k-1]