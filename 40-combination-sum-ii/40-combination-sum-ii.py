class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        anss = []
        candidates.sort()
        N = len(candidates)
        def dfs(index, curr, rem_):
            if rem_ == 0:
                anss.append(curr.copy())
                return
            if rem_ < 0:
                return
            pre = -1
            for i in range(index, N):
                if candidates[i] == pre:
                    continue
                temp = candidates[i]
                curr.append(temp)
                dfs(i + 1, curr, rem_ - temp)
                curr.pop()
                pre = temp

        dfs(0,[],target)
                
        return anss
        