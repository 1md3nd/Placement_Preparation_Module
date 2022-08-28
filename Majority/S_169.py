class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        max1 = -1
        for key in dic:
            if dic[key] > max1:
                max1 = dic[key]
                key1 = key
        return key1