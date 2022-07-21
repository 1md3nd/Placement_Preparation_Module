class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] +=1
        temp = []
        for key in dic:
            if dic[key] > len(nums)//3:
                temp.append(key)
        return temp
            