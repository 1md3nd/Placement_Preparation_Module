class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) < x:
            return -1
        seen = {}
        seen[0] = 0
        
        curr = 0
        for i, num in enumerate(reversed(nums),1):
            curr += num
            seen[curr] = i
        INF = 10 ** 20
        best = INF
        if x in seen:
            best = min(best,seen[x])
        
        curr = 0
        for i, num in enumerate(nums,1):
            curr += num
            if x - curr in seen:
                best = min(best,seen[x-curr]+i)
        if best == INF:
            return -1
        return best
            