class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        INF = 10 ** 20
        minn = INF
        
        ans = ""
        for i in range(len(strs)):
            minn = min(minn,len(strs[i]))
        for i in range(minn):
            prev = strs[0][i]
            flag = True
            for st in strs:
                if st[i] != prev:
                    flag = False
            
            if flag == True:
                ans += st[i]
            else:
                return ans
        return ans
                    
            
                    