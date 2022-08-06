import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # round_ = minutesToTest // minutesToDie
        # res = math.ceil((log(buckets) / log(round_ + 1)))
        # return res
        if buckets == 1:
            return 0
        
        def Check(pigs):
            bucketsCanCheck = (2 ** pigs) - 1
            iteration = (buckets - 1 + bucketsCanCheck - 1) // bucketsCanCheck
            if iteration * minutesToDie <= minutesToTest:
                return True
            round_ = minutesToTest // minutesToDie
            return (round_ + 1) ** pigs >= buckets
        left = 1
        right = buckets
        while left< right:
            mid = (left + right) // 2
            if Check(mid):
                right = mid
            else:
                left = mid + 1
        return left