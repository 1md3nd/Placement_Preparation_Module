class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                min_val_inx = i
                for j in range(i+1,len(nums)):
                    if nums[i-1] < nums[j] <= nums[min_val_inx]:
                        min_val_inx = j
                nums[i-1], nums[min_val_inx] = nums[min_val_inx], nums[i-1]
                l, r = i, len(nums)-1
                while l < r:
                        nums[l], nums[r] = nums[r], nums[l]
                        l+=1; r-=1

                return
        nums.reverse()