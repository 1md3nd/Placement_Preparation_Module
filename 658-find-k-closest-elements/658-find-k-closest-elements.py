from sortedcontainers import SortedList
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        length = len(arr)
        i = bisect.bisect_right(arr, x-1) - 1
        
        j = i + 1
        
        result = SortedList()
        
        while k > 0:
            if j >= length or abs(arr[i] - x) <= abs(arr[j] - x):
                result.add(arr[i])
                i -= 1
            else:
                result.add(arr[j])
                j += 1
            k -= 1
        
        return result