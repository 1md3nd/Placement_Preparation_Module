class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        col = 0
        tri = []
        for i in range(numRows):
            col +=1
            temp = []
            for j in range(col):
                temp.append(0)
            tri.append(temp)
        if numRows == 1:
            tri[0][0] = 1
            return tri
        if numRows == 2:
            tri[0][0] = 1
            tri[1][0] = 1
            tri[1][1] = 1
            return tri
        else:
            tri[0][0] = 1
            tri[1][0] = 1
            tri[1][1] = 1
            ext = 0
            for i in range(2,numRows):
                ext +=1
                tri[i][0] = 1
                for j in range(ext):
                    tri[i][j+1] = tri[i-1][j]+tri[i-1][j+1]
                tri[i][j+2] = 1
            return tri
                    
