class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        summ = 0
        ans = []
        for i in range(1,k+1):
            summ += i
        if summ > n:
            return []
        def check(index, curr, total):
            if k == len(curr) and total == n:
                ans.append(curr.copy())
                return
            for i in range(index,10):
                curr.append(i)
                check(i+1,curr,total+i)
                curr.pop()
        check(1,[],0)
        return ans