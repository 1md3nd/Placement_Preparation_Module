class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = []
        col = []
        row_len = len(matrix)
        col_len = len(matrix[0])
        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        for i in row:
            for j in range(col_len):
                matrix[i][j] = 0
        for j in col:
            for i in range(row_len):
                matrix[i][j] = 0
                
                    
        