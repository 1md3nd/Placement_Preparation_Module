class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        anss = []
        N = len(candidates)
        def dfs(index, curr, total_):
            if total_ == target:
                anss.append(curr.copy())
                return
            if total_ > target or index >= N:
                return
            temp = candidates[index]
            curr.append(temp)
            dfs(index, curr, total_ + temp)
            curr.pop()
            dfs(index + 1, curr, total_)
        dfs(0,[],0)
        return anss
        