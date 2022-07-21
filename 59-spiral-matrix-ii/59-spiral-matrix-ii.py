class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        j = 0
        list1 = []
        count = 1
        for i in range(n):
            temp = []
            for i in range(n):
                temp.append(count)
                count += 1
            list1.append(temp)
        j = 0
        i = 0
        count = 1
        k = 0
        for k in range((n+1)//2):
            for i in range(k,n-k):
                list1[k][i] =count
                count +=1
            for i in range(k+1,n-k):
                list1[i][n-k-1]=count
                count +=1
            for i in range(n-k-2,k-1,-1):
                list1[n-k-1][i]=count
                count +=1
            for i in range(n-k-2,k,-1):
                list1[i][k]=count
                count +=1

        return list1
            
            