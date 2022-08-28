class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        
        for word in words:
            if word == pattern:
                res.append(word)
            else:
                size = len(pattern)
                flag = 0
                pattern_hash = {}
                seen = set()
                for i in range(size):
                    if pattern[i] not in pattern_hash:
                        if word[i] in seen:
                            flag = 1
                            break
                        else:
                            seen.add(word[i])
                            pattern_hash[pattern[i]] = word[i]
                    else:
                        if pattern_hash[pattern[i]] == word[i]:
                            flag = 0
                        else:
                            flag = 1
                            break
                if flag == 0:
                    res.append(word)
        return res
                            
                            
                        
                        
                