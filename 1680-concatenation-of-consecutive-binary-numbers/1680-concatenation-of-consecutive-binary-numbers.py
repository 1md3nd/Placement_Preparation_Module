class Solution:
    def concatenatedBinary(self, n: int) -> int:
        st = ""
        MOD = 10 ** 9 + 7
        for i in range(1,n+1):
            st += bin(i)[2:]
        st = int(st,2)
        return st % MOD