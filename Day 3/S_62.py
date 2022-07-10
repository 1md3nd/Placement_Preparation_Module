class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [1]*n
        for i in range(1,m):
            for j in range(1,n):
                path[j] = path[j-1] + path[j]
        return path[-1]