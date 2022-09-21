class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap,x)
            elif x < heap[0]:
                continue
            elif x >= heap[-1]:
                heapq.heappush(heap,x)
            elif x >= heap[0]:
                heapq.heappush(heap,x)
            while len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        return heap[0]