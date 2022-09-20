class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        seen = {}
        def check(i,j):
            if  i >= M or j  >= N:
                return 0
            if (i,j) not in seen:
                d = check(i+1,j)
                r = check(i,j+1)
                di = check(i+1,j+1)
                if matrix[i][j] == "1":
                    seen[(i,j)] = 1 + min(d,r,di)
                else:
                    seen[(i,j)] = 0
            return seen[(i,j)]
        check(0,0)
        res = 0
        for v in seen.values():
            res = max(res,v * v)
        return res