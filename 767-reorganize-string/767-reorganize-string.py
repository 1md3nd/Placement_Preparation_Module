class Solution:
    def reorganizeString(self, s: str) -> str:
        coll = collections.Counter(s)
        heap = []
        for key, value in coll.items():
            heapq.heappush(heap,(-value, key))
        ans = []
        
        while len(heap) > 0:
            top1v, top1k = heapq.heappop(heap)
            top1v *= -1
            if len(ans) > 0 and ans[-1] == top1k:
                if len(heap) == 0:
                    return ""
                top2v, top2k = heapq.heappop(heap)
                top2v *= -1
                ans.append(top2k)
                top2v -=1
                if top2v != 0:
                    heapq.heappush(heap,(-top2v, top2k))
                if top1v != 0:
                    heapq.heappush(heap,(-top1v, top1k))
            else:
                ans.append(top1k)
                top1v -=1
                if top1v != 0:
                    heapq.heappush(heap,(-top1v, top1k))
        return "".join(ans)
                
        