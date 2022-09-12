class Solution:
    def minGroups(self, inter: List[List[int]]) -> int:
        seen = collections.Counter()
        for left,right in inter:
            seen[left] +=1
            seen[right+1] -=1
        li = sorted(list(seen.keys()))
        best = 0
        curr = 0
        for x in li:
            curr +=seen[x]
            best = max(curr,best)
        return best