class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        n = x
        while x > 0:
            temp = x % 10
            res *= 10
            res += temp
            x //=10
        return res == n