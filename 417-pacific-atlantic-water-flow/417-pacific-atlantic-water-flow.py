class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]
        def df_p(i,j,prev,pacific):
            if i < 0 or j < 0:
                return
            if i >= n or j >= m:
                return
            if pacific[i][j]:
                return
            if heights[i][j] >= prev:
                pacific[i][j] = True
                prev = heights[i][j]
                df_p(i+1,j,prev,pacific)
                df_p(i-1,j,prev,pacific)
                df_p(i,j+1,prev,pacific)
                df_p(i,j-1,prev,pacific)
            return
        def df_a(i,j,prev,atlantic):
            if i < 0 or j < 0 or i == n or j == m or heights[i][j] < prev or atlantic[i][j] == True:
                return
            if heights[i][j] >= prev:
                atlantic[i][j] = True
                prev = heights[i][j]
                df_a(i+1,j,prev,atlantic)
                df_a(i-1,j,prev,atlantic)
                df_a(i,j+1,prev,atlantic)
                df_a(i,j-1,prev,atlantic)
            else:
                return
        for i in range(n):
            df_p(i,0,0,pacific)
            df_a(i,m-1,0,atlantic)
        for j in range(m):
            df_p(0,j,0,pacific)
            df_a(n-1,j,0,atlantic)
        res = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
        return res