class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1/x
        return self.fun(x,n)
    def fun(self,x,n):
        if n == 0:
            return 1
        if x == 0:
            return 0
        temp = self.fun(x,n//2)
        if n % 2 == 0:
            return temp*temp
        else:
            return temp*temp*x
        return temp