class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in range(len(items1)):
            curr = items1[i][0]
            if curr not in dic:
                dic[curr] = items1[i][1]
                
        for i in range(len(items2)):
            curr = items2[i][0]
            if curr not in dic:
                dic[curr] = items2[i][1]
            else:
                dic[curr] += items2[i][1]
        dic_ = []
        for key, value in dic.items():
            temp = [key,value]
            dic_.append(temp)
        dic_.sort()
        return dic_