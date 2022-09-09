class Solution:
    def numberOfWeakCharacters(self, pro: List[List[int]]) -> int:
        pro.sort(key=lambda x: (-x[0],x[1]))
        N = len(pro)
        ans = 0 
        maX = 0
        # print(pro)
        for x,y in pro:
            if maX > y:
                ans +=1
            else:
                maX = y
        return ans
    
            
            