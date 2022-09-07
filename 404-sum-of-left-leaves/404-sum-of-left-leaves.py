# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node,f):
            if node is None:
                return
            if node.left is None and node.right is None:
                if f:
                    ans.append(node.val)
                else:
                    return
            dfs(node.left,True)
            dfs(node.right,False)
        dfs(root,False)
        return sum(ans)