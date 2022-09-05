"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = [root]
        if not root:
            return []
        res = [[root.val]]
        while q:
            size = len(q)
            temp = []
            for _ in range(size):
                head = q.pop(0)
                for child in head.children:
                    if child is not None:
                        temp.append(child.val)
                        q.append(child)
            if temp:
                res.append(temp)
        return res