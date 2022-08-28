class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        x= math.ceil(log(n)/log(3))
        if 3 ** x == n:
            return True
        return False