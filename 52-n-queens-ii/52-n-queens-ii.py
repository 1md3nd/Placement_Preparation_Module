class Solution:
    def totalNQueens(self, n: int) -> int:
        chess = []
        for _ in range(n):
            chess.append([0] * n)
        def safe(chess,row,col):
            # print(chess,row,col)
            if sum(chess[row]) > 1:
                return False
            for i in range(row):
                if chess[i][col] == 1:
                    return False
            for i in range(row+1,n):
                if chess[i][col] == 1:
                    return False
            i, j = row-1,col-1
            while i >= 0 and j >= 0:
                if chess[i][j] == 1:
                    return False
                i -=1
                j -=1
            i, j = row-1,col+1
            while i >= 0 and j < n:
                if chess[i][j] == 1:
                    return False
                i -=1
                j +=1
            i ,j = row+1, col+1
            while i < n and j < n:
                if chess[i][j] == 1:
                    return False
                i +=1
                j +=1
            i,j = row +1, col -1
            while i < n  and j >= 0 :
                if chess[i][j] == 1:
                    return False
                i +=1
                j -=1
            return True
        count = []
        def queen(row):
            if row == n:
                count.append(1)
                return
            for col in range(n):
                if chess[row][col] == 0 and safe(chess,row,col):
                    chess[row][col] = 1
                    queen(row+1)
                    chess[row][col] = 0
        queen(0)
        return len(count)