class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        N = len(num)
        def check(first,second):
            res =[first,second]
            size = len(first) + len(second)
            while size < N:
                temp = int(res[-1]) + int(res[-2])
                res.append(str(temp))
                size += len(res[-1])
            return "".join(res)
        for i in range(1,N):
            for j in range(i+1,N):
                if num[i] == "0" and j - i > 1:
                    break
                first = num[:i]
                second = num[i:j]
                # arr = [int(first),int(second)]
                """
                1|1|2358
                first = 1
                second = 1
                """
                res = check(first,second)
                if res == num:
                    return True
            if num[0] == "0":
                break
        return False