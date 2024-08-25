class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        ans = []
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        sorted_hmap = dict(sorted(hmap.items(), key = lambda x: x[1], reverse=True))
        counter = 0
        for key, value in sorted_hmap.items():
            if counter == k:
                break
            ans.append(key)
            counter += 1
        return ans