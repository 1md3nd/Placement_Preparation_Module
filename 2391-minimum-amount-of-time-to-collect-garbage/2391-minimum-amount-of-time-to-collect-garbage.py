class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        tar = []
        total = 0
        for gar in garbage:
            temp = collections.Counter(gar)
            tar.append(temp)
        for i in range(len(garbage)):
            for value in tar[i].values():
                total += value
        to = ['M','P','G']
        for i in range(1,len(travel)):
            travel[i] += travel[i-1]
        dic = {}
        dic['M'] = True
        dic['P'] = True
        dic['G'] = True
        
        for i in range(len(garbage)-1,0,-1):
            if 'M' in tar[i] and dic['M'] == True:
                dic['M'] = False
                total += travel[i-1]
            if 'P' in tar[i] and dic['P'] == True:
                dic['P'] = False
                total += travel[i-1]
            if 'G' in tar[i] and dic['G'] == True:
                dic['G'] = False
                total += travel[i-1]
        return total