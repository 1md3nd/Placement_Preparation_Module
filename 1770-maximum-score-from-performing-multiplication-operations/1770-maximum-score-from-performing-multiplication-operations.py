class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        N = len(nums)
        M = len(multipliers)
        cache = [[0] *(M)for _ in range(M)]
        has_cache = [[False] * (M) for _ in range(M) ]
        def solve(nums,idx,start):
            if idx == M:
                return 0
            if has_cache[idx][start]:
                return cache[idx][start]
            end = N - (idx - start) - 1
            # print(idx,start,end,N)
            left = nums[start] * multipliers[idx] + solve(nums,idx+1,start+1)
            right = nums[end] * multipliers[idx] + solve(nums,idx+1,start)
            has_cache[idx][start] = True
            cache[idx][start] = max(left,right)
            return cache[idx][start]
        return solve(nums,0,0)