class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        while k > 0:
            temp = nums[i]
            nums.pop()
            nums.insert(0,temp)
            k -=1
        
            