class Solution:
    def climbStairs(self, n: int) -> int:
#### To Print all thecombinations
        # def comb(num,res):
        #     if num < 0:
        #         return 
        #     if num == 0:
        #         print(res)
        #         return
        #     comb(num-1,res + "1")
        #     comb(num-2,res + "2")
        # comb(n,"")
#### To count pattern
        x_ = 1
        y_ = 1
        for _ in range(n-1):
            temp = x_
            x_ = x_ + y_
            y_ = temp
        return x_
