class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        self.count = 0
        MOD = 10 ** 9 + 7
        if startPos + k == endPos:
            return 1
        # elif startPos + k < endPos:
        memory = {}
        def solve(k,curr):
            if (k,curr) in memory:
                return memory[(k,curr)]
            if k == 0:
                if curr == endPos:
                    memory[(k,curr)] = 1
                    return 1
                else:
                    memory[(k,curr)] = 0
                    return 0
            if k < 0:
                memory[(k,curr)] = 0
                return 0
            memory[k,curr] = (solve(k-1,curr+1) + solve(k-1,curr-1))
            return memory[(k,curr)]
        solve(k,startPos)
        return memory[(k,startPos)] % MOD
            