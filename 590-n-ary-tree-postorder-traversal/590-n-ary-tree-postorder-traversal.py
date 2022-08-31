"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ########
        res = []
        if not root:
            return res
        def solve(root):
            for child in root.children:
                solve(child)
            res.append(root.val)
            return
        solve(root)
        return res