class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1 for _ in range(N)]
        prevL = 1
        for i in range(N):
            res[i] *= prevL
            prevL *= nums[i]
        prevR = 1
        for i in range(N-1,-1,-1):
            res[i] *= prevR
            prevR *= nums[i]
        return res
            