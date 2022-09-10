class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # N = len(prices)
        # if N == 0:
        #     return 0
        # dp = [(0,0)] * N
        # dp[0] = (prices[0],0)
        # for i in range(1,N):
        #     dp[i] = (min(dp[i-1][0] , prices[i]), max(prices[i] - dp[i-1][0], dp[i-1][1]))
        # return dp[N - 1][1]
        N = len(prices)
        buy = prices[0]
        sell = buy
        res = 0
        for i in range(1,N):
            if prices[i] > buy:
                res = max(prices[i] - buy,res)
            elif prices[i] < buy:
                buy = prices[i]
        return res