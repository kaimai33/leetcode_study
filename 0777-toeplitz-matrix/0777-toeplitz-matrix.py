class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def checkDiag(r, c):
            curr_val = matrix[r][c]
            for i in range(min(len(matrix) - r, len(matrix[0]) - c)):
                if matrix[r+i][c+i] != curr_val:
                    return False
            return True
        # check top row diags
        for i in range(len(matrix)):
            if not checkDiag(i, 0):
                return False
        # check left col diags
        for i in range(len(matrix[0])):
            if not checkDiag(0, i):
                return False
        
        return True