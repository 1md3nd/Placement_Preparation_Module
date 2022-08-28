class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        N = len(mat)
        C = len(mat[0])
        def org(row,col):
            dic = {}
            r = row
            c = col
            while r < N and c < C:
                if mat[r][c] in dic:
                    dic[mat[r][c]] += 1
                else:
                    dic[mat[r][c]] = 1
                r += 1
                c += 1
            r = row
            c = col
            for i in range(101):
                if i in dic:
                    val = dic[i]
                    while val > 0:
                        mat[r][c] = i
                        val -=1
                        r +=1
                        c +=1
                        
        for i in range(N):
            org(i,0)
        for j in range(1,C):
            org(0,j)
        return mat