class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                temp_sum1 = nums[i] + nums[j]
                p_1 = j+1
                p_2 = len(nums)-1
                while p_1 < p_2:
                    temp_sum2 = temp_sum1 + nums[p_1] + nums[p_2]
                    if temp_sum2 == target:
                        result.add((nums[i],nums[j],nums[p_1],nums[p_2]))
                        p_1 +=1
                        p_2 -=1
                    elif temp_sum2 > target:
                        p_2 -=1
                    else:
                        p_1 +=1
        return result