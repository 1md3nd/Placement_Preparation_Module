class Solution:
    def permuteUnique(self, num: List[int]) -> List[List[int]]:
        # hash_ = {}
        def per(nums,res):
            final = []
            if len(nums) == 1:
                return [[nums[0]]]
            for i in range(len(nums)):
                mid = nums[i]
                other =(nums[:i]) + nums[i+1:]
                res = per(other,[])
                for x in res:
                    x.append(mid)
                    # if str(x) not in hash_:
                    #     hash_[str(x)] = 1
                    final.append(x)
            # print(final)
            return final
        unique = {}
        result = per(num,[]) 
        res = []
        for x in result:
            temp = ""
            for i in x:
                temp += str(i)
            if temp not in unique:
                unique[temp] = 1
                res.append(x)
        return res