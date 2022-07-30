class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        temp_hash = Counter()
        for word in words2:
            temp_hash |= Counter(word)
        for word in words1:
            temp = temp_hash - Counter(word)
            if not temp:
                res.append(word)
        return res