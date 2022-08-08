class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        L = [1] * N
        for i in range(N-1,-1,-1):
            for j in range(i+1,N):
                if nums[i] < nums[j]:
                    L[i] = max(L[i],1 + L[j])
        return max(L)
    
        