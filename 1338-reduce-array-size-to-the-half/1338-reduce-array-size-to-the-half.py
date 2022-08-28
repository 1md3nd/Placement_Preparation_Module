class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        counts = sorted(count.values(), key = lambda x : -x)
        N = len(arr)
        ans = 0
        for i in range(len(counts)):
            ans += counts[i]
            if ans >= N//2:
                return i + 1