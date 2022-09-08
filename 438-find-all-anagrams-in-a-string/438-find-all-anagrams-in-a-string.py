class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash_ = collections.Counter(p)
        j = 0
        res = []
        h2 = {}
        for i in range(len(s)):
            if s[i] not in hash_:
                j = i+1
                h2 = {}
                continue
                
            elif s[i] in h2:
                h2[s[i]] +=1
                while h2[s[i]] > hash_[s[i]]:
                    h2[s[j]] -=1
                    j +=1
            else:
                h2[s[i]] = 1
            # print(h2)

            if h2 == hash_:
                res.append(j)
                h2[s[j]]-=1
                j +=1
        return res
            
            