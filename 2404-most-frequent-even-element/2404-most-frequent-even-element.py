class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        hash_ =  {}
        for num in nums:
            if num % 2 == 0:
                if num in hash_:
                    hash_[num] +=1
                else:
                    hash_[num] = 1
        ans = -1
        mX = 0
        # print(hash_)
        for k, v in hash_.items():
            if mX < v:
                ans = k
                mX = v
            elif mX == v:
                if k < ans:
                    ans = k
        return ans
                    
            