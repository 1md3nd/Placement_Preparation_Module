class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        target = {}
        for ch in t:
            target[ch] = 1 + target.get(ch,0)
        window = {}
        have, need = 0, len(target)
        left = 0
        INF = 10 ** 20
        ans, ansL = [-1,-1], INF
        for  right in range(len(s)):
            ch = s[right]
            window[ch] = 1 + window.get(ch,0)
            if ch in target and window[ch] == target[ch]:
                have += 1
            while have == need:
                if (right - left + 1) < ansL:
                    ansL = (right - left + 1)
                    ans = [left,right]
                window[s[left]] -=1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1
                left +=1
        left, right = ans
        return s[left:right+1] if ansL != INF else ""
                    
            