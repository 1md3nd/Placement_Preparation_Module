class Solution:
    def generateTheString(self, n: int) -> str:
        ans = ""
        if n%2 != 0:
            for _ in range(n):
                ans += 'a'
        else:
            for _ in range(n-1):
                ans += 'x'
            ans += 'y'
        return ans