class Solution:
    def numDecodings(self, s: str) -> int:
        prepre, pre = 0, 1
        for i, ch in enumerate(s):
            curr = 0
            if ch!='0':
                curr += pre
            if i > 0 and (s[i-1]=='1' or (s[i-1]=='2' and ch<'7')):
                curr += prepre
            prepre, pre = pre, curr
        return pre