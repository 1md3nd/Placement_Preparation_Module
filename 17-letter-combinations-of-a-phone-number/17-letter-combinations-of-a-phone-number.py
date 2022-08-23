class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dist = {
            "1" : "",
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
            "0" : ""
        }
        def recursion(num):
            if len(num) == 0:
                return
            
            if len(num) == 1:
                comb = []
                for i in range(len(dist[num])):
                    comb.append(dist[num][i])
                return comb
            digit = dist[num[0]]
            # print(digit,num[0],num[1:])
            combination = recursion(num[1:])
            # print(combination)
            res = []
            for i in range(len(digit)):
                temp = digit[i]
                # print(temp)
                for x in combination:
                    res.append(temp + x)
            return res
        return recursion(digits)
            
            
