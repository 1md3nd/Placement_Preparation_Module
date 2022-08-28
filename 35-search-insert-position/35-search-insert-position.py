class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, value in enumerate(nums):
            if value == target:
                return i
            elif target < value:
                return i
            elif target > nums[len(nums)-1]:
                return len(nums)
    
                
            
            