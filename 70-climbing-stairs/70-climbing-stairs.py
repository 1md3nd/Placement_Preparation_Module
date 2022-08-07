class Solution:
    def climbStairs(self, n: int) -> int:
        x_ = 1
        y_ = 1
        for _ in range(n-1):
            temp = x_
            x_ = x_ + y_
            y_ = temp
        return x_