class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rowIdx = 0
        rowOnes = 0
        for i in range(len(mat)):
            if sum(mat[i]) > rowOnes:
                rowOnes = sum(mat[i])
                rowIdx = i
        return [rowIdx, rowOnes]