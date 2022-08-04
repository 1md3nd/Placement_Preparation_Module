class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        INF = 10 ** 20
        ans = []
        min_rem = INF
        def cal(x):
            nonlocal ans
            nonlocal min_rem
            i = 1
            while i * i <= x:
                if x%i == 0:
                    temp = abs(i - x // i)
                    if temp < min_rem:
                        min_rem = temp      
                        ans = [i, x//i]
                i +=1
            
        cal(num +1)
        cal(num +2)
        return ans