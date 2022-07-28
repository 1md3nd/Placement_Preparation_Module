class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                break
            else:
                start = -1
        if start == -1:
            return [-1,-1]
        end = start
        for j in range(start,len(nums)):
            if nums[j] != target:
                end = j-1
                break
            else:
                end = j
        return [start,end]
            