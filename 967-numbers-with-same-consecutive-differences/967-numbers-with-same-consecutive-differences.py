class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        def rec(num):
            if num in res:
                return
            if len(num) == n:
                res.append(num)
                return
            for i in range(10):
                if len(num) == 0:
                    if i == 0:
                        continue
                    else:
                        rec(str(i))
                else:
                    # sm = int(num[-1]) + k
                    # if sm < 10:
                    #     rec(num+str(sm))
                    diff = abs(int(num[-1]) - i)
                    if diff == k:
                        rec(num+str(i))
        rec("")
        res = [int(i) for i in res]
        return res
        # for i in range(10):
        #     # if x == 0:
        #     #     continue
        #     # else:
        #     #     ans += str(x)
        #     ans = ""
        #     for x in range(n):
        #         if i == 0 and x == 0:
        #             break
        #         else:
        #             if x == 0:
        #                 ans += str(i)
        #                 continue
        #             else:
        #                 # print(i,x,ans)
        #                 if int(ans[x-1]) < k:
        #                     res = k + int(ans[x-1])
        #                     if res >= 10:
        #                         break
        #                     else: ans += str(res)
        #                 else:  
        #                     ans += str(abs(int(ans[x-1]) - k))
        #     if len(ans) == n:
        #         out.append(ans)
        # return out
