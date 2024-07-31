class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref) == 1:
            return pref
        ans = []
        ans.append(pref[0])
        for i in range(1, len(pref)):
            ans.append(pref[i-1] ^ pref[i])
        
        return ans
        