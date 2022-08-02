class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        left, right = matrix[0][0], matrix[N-1][N-1]
        
        # Does target have k-1 smaller number
        #O(N log N)
        def istarget(target):
            count = 0
            for row in matrix:
                count += bisect.bisect_left(row, target)
            return count <= k-1
        
        #O(R) -> R = 10**9 number of iterations
        #O(N log N log R)
        while left < right:
            mid = (left+right+1)//2
            if istarget(mid):
                left = mid
            else:
                right = mid - 1
        return left