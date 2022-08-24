class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        maxx = math.floor(log(10**7)//log(3))
        for i in range(maxx,-1,-1):
            x = 3 ** i
            if x <= n:
                n -= x
                # print(i)
            if n == 0:
                return True
        return False