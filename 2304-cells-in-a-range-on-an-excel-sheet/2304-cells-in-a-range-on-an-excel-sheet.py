class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1, _, c2, r2 = s
        ans = []


        for i in range(ord(c1), ord(c2) + 1):
            for j in range(int(r1), int(r2) + 1):
                ans.append(str(chr(i) + str(j)))
        
        return ans