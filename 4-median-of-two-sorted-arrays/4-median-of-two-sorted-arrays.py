import heapq
class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        min_heap = []
        max_heap = []
        temp_heap = []
        def Fix_Heap(x):
            if len(max_heap) == 0 or abs(max_heap[0]) > x:
                heapq.heappush(max_heap, -x)
            else:
                heapq.heappush(min_heap, x)
                
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap,-(heapq.heappop(max_heap)))
            elif len(max_heap) < len(min_heap):
                heapq.heappush(max_heap,-(heapq.heappop(min_heap)))
        
        def Find_Median():
            if len(max_heap) == len(min_heap):
                return -max_heap[0]/2 + min_heap[0]/2
            else:
                return -max_heap[0]
        for i in nums1:
            heapq.heappush(temp_heap,i)
        for i in nums2:
            heapq.heappush(temp_heap,i)
        while temp_heap:
            Fix_Heap(heapq.heappop(temp_heap))
        return Find_Median()
    
        
                    
                