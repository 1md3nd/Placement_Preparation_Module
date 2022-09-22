class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        i = 0
        j = 0
        res = 1
        while i < len(s)-1:
            print(i,j)
            if ord(s[i+1]) - ord(s[i]) == 1:
                i +=1
                res = max(res,i-j+1)
            else:
                i+=1
                j = i
                
        # res = max(res,i-j)
        return res