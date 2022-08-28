class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for que in queries:
            count = 0
            summ = 0
            for i in range(len(nums)):
                summ += nums[i]
                count += 1
                if summ == que:
                    break
                if summ < que:
                    continue
                else:
                    summ -= nums[i]
                    count -=1
            ans.append(count)
        return ans
            