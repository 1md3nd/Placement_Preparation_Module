class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_ = collections.Counter(s)
        for i in range(len(s)):
            if hash_[s[i]] > 1:
                continue
            return i
        return -1
            