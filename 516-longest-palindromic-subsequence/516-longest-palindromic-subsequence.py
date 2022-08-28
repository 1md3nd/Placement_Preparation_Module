class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text2 = s[::-1]
        text1 = s
        # print(text1,text2)
        one = len(text1)
        two = len(text2)
        mat = [[0 for j in range(two + 1)] for i in range(one + 1)]
        for i in range(one-1,-1,-1):
            for j in range(two - 1, -1 ,-1):
                if text1[i] == text2[j]: 
                    mat[i][j] =  1 + mat[i+1][j+1]
                else:
                    mat[i][j] = max(mat[i+1][j], mat[i][j+1])
        return mat[0][0]