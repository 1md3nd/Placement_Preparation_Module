class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        tList = list(target)
        N = len(tList)
        sList = list(stamp)
        S = len(sList)
        count = 0
        visited = [False] * N
        res = []
        def canReplace(position):
            for i in range(S):
                if tList[position + i] != sList[i] and tList[position + i] != "?":
                    return False
            return True
        def replace(position):
            nonlocal count
            for i in range(S):
                if tList[position + i] != "?":
                    tList[position + i] = "?"
                    count += 1
            return count

        while count != N:
            change =  True
            for i in range(N-S+1):
                # print(tList)
                if not visited[i] and canReplace(i):
                    visited[i] = True
                    change = False
                    count = replace(i)
                    res.append(i)
                    # print(tList,res)
                    break
                    # if count == N:
                    #     break
            if change:
                return []
    
        return reversed(res)
        
            