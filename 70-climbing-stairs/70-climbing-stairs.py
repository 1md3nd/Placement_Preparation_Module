class Solution:
    def climbStairs(self, n: int) -> int:
        x_two = 1
        x_one = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in range(n-2):
            x = x_two + x_one
            x_two = x_one
            x_one = x
        return x_one