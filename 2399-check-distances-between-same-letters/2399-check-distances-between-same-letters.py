class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        n = len(s)
        for i in range(n-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if distance[ord(s[i]) - 97]  != (j - i - 1):
                        return False
                    else:
                        break
        return True
        # for key in dic.keys():
        #     if distance[ord(key) - 97] == dic[key]:
        #         continue
        #     else:
        #         return False
        # return True