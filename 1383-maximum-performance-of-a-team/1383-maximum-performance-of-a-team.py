class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        merge = sorted(zip(efficiency,speed),reverse = True)
        sumS , ans = 0,0
        MOD = 10 ** 9 + 7
        heap = []
        for eff, spd in merge:
            heapq.heappush(heap,spd)
            sumS += spd
            if len(heap) > k:
                sumS -= heapq.heappop(heap)
            ans = max(ans,sumS*eff)
        return ans % MOD