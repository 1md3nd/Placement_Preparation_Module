class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        i = -1
        j = -1
        indexs = {}
        n = len(s)
        while True:
            f1 = False
            f2 = False
            while i < n - 1:
                f1 = True
                i += 1
                ch = s[i]
                indexs[ch] = indexs.get(ch, 0) + 1
                if indexs[ch] == 2:
                    break
                else:
                    length = i - j
                    if length > ans:
                        ans = length
            while j < i:
                f2 = False
                j += 1
                ch = s[j]
                indexs[ch] = indexs[ch] - 1
                if indexs[ch] == 1:
                    break
            if f1 == False and f2 == False:
                break
        return ans
                