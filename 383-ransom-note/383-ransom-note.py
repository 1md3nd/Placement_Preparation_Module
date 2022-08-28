class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_ = collections.Counter(magazine)
        # print(hash_)
        for i in range(len(ransomNote)):
            if ransomNote[i] not in hash_:
                return False
            hash_[ransomNote[i]] -= 1
            # print(hash_)
            if hash_[ransomNote[i]] < 0:
                return False
        return True