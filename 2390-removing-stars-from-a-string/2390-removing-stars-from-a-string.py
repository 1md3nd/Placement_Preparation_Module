class Solution:
    def removeStars(self, s: str) -> str:
        ans = "" 
        count = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] != "*":
                if count == 0:
                    ans += s[i]
                if count != 0:
                    count -=1
                    continue
            if s[i] == "*":
                count += 1
    
        return ans[::-1]