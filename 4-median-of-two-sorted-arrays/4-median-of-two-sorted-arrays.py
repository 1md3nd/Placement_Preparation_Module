class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size_1 = len(nums1)
        size_2 = len(nums2)
        res = []
        i, j = 0, 0
        while i < size_1 and j < size_2:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1 
            else:
                res.append(nums2[j])
                j += 1
        res = res + nums1[i:] + nums2[j:]
        #print(res)
        length = len(res)
        if length%2 !=0:
            mid = length//2
            print(mid)
            return float(res[mid])
        else:
            mid = length//2
            mid -=1
            #print(res[mid],res[mid+1])
            sum1 = res[mid] + res[mid+1]
            sum1 /=2
            return float(sum1)