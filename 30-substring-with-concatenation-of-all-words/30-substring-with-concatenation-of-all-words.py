import collections
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N = len(s)
        M = len(words)
        W = len(words[0])
        ans = []
        def adjust(word, count, hash_):
            hash_[word] += count
            if hash_[word] == 0:
                del hash_[word]
        
        for start in range(W):
            curr = start
            if curr + W * M > N:
                continue
            hash_ = collections.Counter(words)
            curr = start
            for i in range(M):
                adjust(s[curr : curr + W], -1, hash_)
                curr += W
            if len(hash_) == 0:
                ans.append(curr - (W * M))
            while curr + W <= N:
                adjust(s[curr : curr + W], -1, hash_)
                adjust(s[curr - (M * W) : curr - (M - 1) * W], +1, hash_)
                curr += W
                if len(hash_) == 0:
                    ans.append(curr - W * M)
        return ans
                    
                    
                
                
                