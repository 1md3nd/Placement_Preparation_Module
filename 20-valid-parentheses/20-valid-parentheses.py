class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = ['()','{}','[]']
        for x in s:
            if x in '({[':
                stack.append(x)
            elif stack == [] or stack.pop()+x not in pairs:
                return False
        return stack == []
                
                                                                                                                                                                                                                                                                                                                                    