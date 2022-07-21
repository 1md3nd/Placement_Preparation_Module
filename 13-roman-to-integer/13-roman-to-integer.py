class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        rep = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        sub = {
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }
        for key, val in sub.items():
            if key in s:
                s = s.replace(key,'')
                res += int(val)
        for x in s:
            res += int(rep[x])
        return res