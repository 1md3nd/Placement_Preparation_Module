class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # Matrix Exponentiation
        MOD = 10 ** 9 + 7
        curr = [1]*5
        prev = curr
        for _ in range(1,n):
            curr = [0] * 5
            
            # next character is 'a' -> e'i'u
            curr[0] = (prev[1] + prev[2] + prev[4]) % MOD
            # e -> a'i
            curr[1] = (prev[0] + prev[2]) % MOD
            # i -> e'o
            curr[2] = (prev[1] + prev[3]) % MOD
            # o -> i'u
            curr[3] = prev[2] % MOD
            # u -> a'i
            curr[4] =  (prev[2] + prev[3]) % MOD
            
            prev = curr
            
        return sum(curr) % MOD