class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict1, dict2, dict3, dict4 = {}, {}, {}, {}
        dict12, dict34 = {}, {}
        ans = 0
        n = len(nums1)
        for i in range(n):
            dict1[nums1[i]] = dict1.get(nums1[i], 0) + 1
            dict2[nums2[i]] = dict2.get(nums2[i], 0) + 1
            dict3[nums3[i]] = dict3.get(nums3[i], 0) + 1
            dict4[nums4[i]] = dict4.get(nums4[i], 0) + 1
        for n1 in dict1:
            for n2 in dict2:
                dict12[n1 + n2] = dict12.get(n1 + n2, 0) + (dict1[n1] * dict2[n2])
        for n3 in dict3:
            for n4 in dict4:
                dict34[n3 + n4] = dict34.get(n3 + n4, 0) + (dict3[n3] * dict4[n4])
        for n12 in dict12:
            for n34 in dict34:
                if n12 + n34 == 0:
                    ans += dict12[n12] * dict34[n34]
        return ans
        
        
