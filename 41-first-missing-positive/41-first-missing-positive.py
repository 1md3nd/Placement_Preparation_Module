class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        minn = 0
        for i in range(len(nums)):
            if nums[i] <= 0:
                minn = i + 1
                continue
        # print(nums)
        if minn >= len(nums) or nums[minn] != 1:
            return 1
        prev = nums[minn]
        
        for i in range(minn + 1,len(nums)):
            # print(prev, nums[i])
            if nums[i] == prev:
                continue
            elif nums[i] - prev != 1:
                return prev + 1
            prev = nums[i]
        return prev + 1