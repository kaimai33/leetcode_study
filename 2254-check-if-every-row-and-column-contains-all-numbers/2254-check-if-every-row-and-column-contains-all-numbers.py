class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        # check rows
        for i in range(len(matrix)):
            curr_row = set()
            for j in range(len(matrix[0])):
                if 1 <= matrix[i][j] <= n:
                    curr_row.add(matrix[i][j])
                else:
                    return False
            if len(curr_row) != n:
                return False

        # check cols
        for j in range(len(matrix[0])):
            curr_col = set()
            for i in range(len(matrix)):
                if 1 <= matrix[i][j] <= n:
                    curr_col.add(matrix[i][j])
                else:
                    return False
            if len(curr_col) != n:
                return False
        
        return True