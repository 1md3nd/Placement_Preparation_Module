import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        round_ = minutesToTest // minutesToDie
        res = math.ceil((log(buckets) / log(round_ + 1)))
        return res