class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        M = (N + 1) // 2
        M2 = N // 2
        for i in range(M):
            for j in range(M2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[N - 1 - j][i]
                matrix[N - 1 - j][i] = matrix[N - i - 1][N - 1 - j]
                matrix[N - i - 1][N - 1 - j] = matrix[j][N - 1 - i]
                matrix[j][N - 1 - i] = temp
                
                
            