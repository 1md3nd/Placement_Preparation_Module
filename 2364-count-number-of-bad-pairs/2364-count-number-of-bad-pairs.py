class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        summ = 0
        b = []
        dic = {}
        for i in range(len(nums)):
            temp = nums[i] - i
            b.append(temp)
            if temp not in dic:
                dic[temp] = 1
            else:
                dic[temp] += 1
        # print(b)
        # print(dic)
        N = len(nums)
        for i in range(len(b)):
            no_same = N - dic[b[i]]
            # print(no_same,nums[i])
            N -=1
            summ += no_same
            dic[b[i]] -=1
        return summ
            