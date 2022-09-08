class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        q = []
        count = 0
        summ = nums[0]
        q.append(nums[0])
        dp = [0] * N
        dp[0] = nums[0]
        prev = 0
        for i in range(1,N):
            dp[i] = dp[i-1] + nums[i]
        print(dp)
        dic = {0:1}
        for i in range(N):
            if dp[i]-k in dic:
                count += dic[dp[i]-k]
            if dp[i] not in dic:
                dic[dp[i]] = 1
            else:
                dic[dp[i]] +=1
        return count
                
                    