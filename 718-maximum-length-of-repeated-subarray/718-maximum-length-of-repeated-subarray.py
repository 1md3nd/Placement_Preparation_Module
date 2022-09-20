class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        M = len(nums1)
        N = len(nums2)
        dp = [[0] * N for _ in range(M)]
        score = 0
        for i in range(M):
            for j in range(N):
                if nums1[i] == nums2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    elif dp[i-1][j-1] != 0:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = 1
                score = max(score,dp[i][j])
        # for x in dp:
        #     print(x)
        return score