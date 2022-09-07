class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        def check(seen):
            for i in seen:
                if hash_[s[i]] != 0:
                    return False
            res.append(len(seen))
            return True
        hash_ = collections.Counter(s)
        seen = []
        for i in range(len(s)):
            x = s[i]
            hash_[x] -=1
            seen.append(i)
            if hash_[x] == 0:
                if check(seen):
                    seen = []
        return res
        
            
                