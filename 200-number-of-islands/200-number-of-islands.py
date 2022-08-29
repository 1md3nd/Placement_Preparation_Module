class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(False)
            seen.append(temp)
        def dfs(i,j):
            nonlocal n
            nonlocal m
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if seen[i][j] == True:
                return False
            seen[i][j] = True
            if grid[i][j] == "0":
                return
            # print(i+1,j+1)
            if grid[i][j] == "1":
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            return True
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    if dfs(i,j):
                        count +=1
                    
        return count
                