class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        m = len(grid)
        n = len(grid[0])
        seen = set()
        def makerot(i,j,q):
            if (i,j) in seen:
                return
            seen.add((i,j))
            if i+1 < m and (i+1,j) not in seen:
                if grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    q.append((i+1,j))
                # elif grid[i+1][j] == 2:
                #     q.append((i+1,j))
            if i-1 >= 0 and (i-1,j) not in seen:
                if grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    q.append((i-1,j))
                # elif grid[i-1][j] == 2:
                #     q.append((i-1,j))
            if j+1 < n and (i,j+1) not in seen:
                if grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    q.append((i,j+1))
                # elif grid[i][j+1] == 2:
                #     q.append((i,j+1))
            if j-1 >= 0 and (i,j-1) not in seen:
                if grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    q.append((i,j-1))
                # elif grid[i][j-1] == 2:
                #     q.append((i,j-1))
            return
        one = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    one +=1
        if not q and one:
            return -1
        if not q:
            return 0
        count = -1
        while q:
            size = len(q)
            for _ in range(size):
                i,j = q.pop(0)
                if grid[i][j] == 2:
                    makerot(i,j,q)
            # print(grid,q,seen)
            count += 1
        # print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return count
                    