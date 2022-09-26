class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = [i for i in range(26)]
        def unionFind(x):
            if parents[x] != x:
                parents[x] = unionFind(parents[x])
            return parents[x]
        def union(x,y):
            lx = unionFind(x)
            ly = unionFind(y)
            parents[lx] = ly
        for equation in equations:
            if equation[1] == "!":
                continue
            else:
                first = ord(equation[0]) - ord("a")
                second = ord(equation[3]) - ord("a")
                union(first,second)
            
        for equation in equations:
            if equation[1] != "!":
                continue
            else:
                first = ord(equation[0]) - ord("a")
                second = ord(equation[3]) - ord("a")
                if unionFind(first) == unionFind(second):
                    return False
        return True