# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(root,curr):
            if root is None:
                res.append(curr)
                # print(curr)
                return
            dfs(root.left,curr+1)
            dfs(root.right,curr+1)
        dfs(root,0)
        return max(res)
                