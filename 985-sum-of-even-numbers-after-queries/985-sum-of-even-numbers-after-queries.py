class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                total += nums[i]
        res = []
        for querie in queries:
            val = querie[0]
            index = querie[1]
            if nums[index] % 2 == 0:
                total -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                total += nums[index]
            res.append(total)
        return res
            