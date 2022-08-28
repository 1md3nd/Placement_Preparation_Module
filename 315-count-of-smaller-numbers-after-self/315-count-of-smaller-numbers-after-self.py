class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        res = []
        for x in nums:
            temp = bisect_left(arr,x)
            res.append(temp)
            del arr[temp]
        return res
            
            