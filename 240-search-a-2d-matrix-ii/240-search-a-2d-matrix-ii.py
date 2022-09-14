class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        def check(arr,l,r,target):
            # print(arr,l,r)
            while l < r:
                m = (l+r)//2
                if arr[m] == target:
                    return True
                if arr[m] > target:
                    l = l
                    r = m
                else:
                    l = m+1
                    r = r
            return False

        for i in range(M):
            if matrix[i][0] > target:
                return False
            else:
                if check(matrix[i],0,N,target):
                    return True
        return False
            
                