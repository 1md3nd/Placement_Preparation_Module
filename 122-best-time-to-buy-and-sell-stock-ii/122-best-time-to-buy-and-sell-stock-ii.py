class Solution:
    def maxProfit(self, p: List[int]) -> int:
        N = len(p)
        buy = p[0]
        ans = [0 for _ in range(N)]
        for i in range(1,N):
            if p[i] > p[i-1]:
                ans[i] = p[i] - p[i-1]
            else:
                ans[i] = 0
        # print(ans)
        return sum(ans)
        # print(ans)
            