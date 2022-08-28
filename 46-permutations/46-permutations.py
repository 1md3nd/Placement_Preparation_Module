class Solution:
    def permute(self, num: List[int]) -> List[List[int]]:
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
                    final.append(x)
            # print(final)
            return final
        return per(num,[])