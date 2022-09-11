class Solution:
    def partitionString(self, s: str) -> int:
        N = len(s)
        j = 0
        hash_ = {}
        count = 0
        for i in range(N):
            if s[i] not in hash_:
                hash_[s[i]] = 1
            else:
                hash_ = {}
                count +=1
                hash_[s[i]] = 1
                j = i
        count +=1
        return count
                
        
                