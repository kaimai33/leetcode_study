class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        length = len(A)
        ans = []
        for i in range(length):
            setA.add(A[i])
            setB.add(B[i])
            ans.append(len(setA.intersection(setB)))
        return ans