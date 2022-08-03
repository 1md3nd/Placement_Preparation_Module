import heapq
class Solution:
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        min_heap = []
        max_heap = []
        temp_heap = []
        def Fix_Heap(x):
            if len(max_heap) == 0 and len(min_heap) == 0:
                heapq.heappush(min_heap, -x)
            else:
                if x <= -min_heap[0]:
                    heapq.heappush(min_heap, -x)
                else:
                    heapq.heappush(max_heap, x)
            if len(min_heap) > len(max_heap) + 1:
                heapq.heappush(max_heap,-(heapq.heappop(min_heap)))
            elif len(min_heap) < len(max_heap):
                heapq.heappush(min_heap,-(heapq.heappop(max_heap)))
        
        def Find_Median():
            if len(max_heap) == len(min_heap):
                return -min_heap[0]/2 + max_heap[0]/2
            elif len(max_heap) > len(min_heap):
                return max_heap[-1]
            else:
                return -min_heap[0]
        for i in nums1:
            heapq.heappush(temp_heap,i)
        for i in nums2:
            heapq.heappush(temp_heap,i)
        print(temp_heap)
        while temp_heap:
            Fix_Heap(heapq.heappop(temp_heap))
            # print(max_heap,min_heap)
        
        return Find_Median()
    
        
                    
                