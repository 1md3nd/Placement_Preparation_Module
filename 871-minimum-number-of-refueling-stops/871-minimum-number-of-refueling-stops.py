class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        heap = []
        count = 0
        INF = 10 ** 20
        stations.append([target, INF])
        previous = 0
        for current, currFuel in stations:
            startFuel -= (current - previous)
            while heap and startFuel < 0:
                startFuel += -heapq.heappop(heap)
                count += 1
            if startFuel < 0:
                return -1
            heapq.heappush(heap,-currFuel)
            previous = current
        return count