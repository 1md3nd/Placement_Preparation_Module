class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store = {}
        for x in s:
            if x not in store:
                store[x] = 1
            else:
                store[x] +=1
        for x in t:
            if x not in store:
                return False
            store[x] -=1
            if store[x] < 0:
                return False
        for key in store:
            if store[key] != 0:
                return False
        return True