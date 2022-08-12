class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # TIme -> O(N) * O(K)
        # Space -> O(N+1)
        n = len(arr)
        dp = [0] * (n+1)
        for index in range(n-1,-1,-1):
            summ = 0
            count = 0
            INF = 10 ** 20
            MaxAns = -INF
            mxa = -INF
            for j in range(index,min(index+k,n)):
                count +=1
                mxa = max(mxa,arr[j])
                summ = count * mxa + dp[j+1]
                MaxAns = max(summ,MaxAns)
            dp[index] = MaxAns
        return dp[0]