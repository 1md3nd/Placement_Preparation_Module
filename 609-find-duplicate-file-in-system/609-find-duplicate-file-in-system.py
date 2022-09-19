class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        res = []
        
        for path in paths:
            arr = path.split()
            directory = arr[0]
            for i in range(1, len(arr)):
                num, filecontents = arr[i].split('.')
                seen[filecontents].append(f"{directory}/{num}.txt")
        for v in seen.values():
            if len(v) > 1:
                res.append(v)
        return res