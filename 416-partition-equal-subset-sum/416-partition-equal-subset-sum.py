class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        if sum(nums) % 2  != 0:return False
        else:target = sum(nums)//2
        seen = {0}
        for num in nums:
            seen |= {(num + val) for val in seen}
        return target in seen