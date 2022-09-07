# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # ans = []
        def dfs(node,f):
            res = 0
            if node is None:
                return res
            if node.left is None and node.right is None:
                if f:
                    res += node.val
                else:
                    return res
            res += dfs(node.left,True)
            res += dfs(node.right,False)
            return res
        res = dfs(root,False)
        return res