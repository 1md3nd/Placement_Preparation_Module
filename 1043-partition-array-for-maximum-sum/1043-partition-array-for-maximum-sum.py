class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1] * n
        def helper(index):
            nonlocal dp
            nonlocal n
            if index == n:
                return 0
            if dp[index] != -1:
                return dp[index]
            summ = 0
            count = 0
            INF = 10 ** 20
            MaxAns = -INF
            mxa = -INF
            for j in range(index,min(index+k,n)):
                count +=1
                mxa = max(mxa,arr[j])
                summ = count * mxa + helper(j + 1)
                MaxAns = max(summ,MaxAns)
            dp[index] = MaxAns
            return MaxAns
        return helper(0)