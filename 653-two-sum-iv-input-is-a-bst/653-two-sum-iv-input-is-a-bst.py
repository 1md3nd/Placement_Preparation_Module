# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = False
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def dfs(node,ans):
            if self.ans:
                return
            if node is None:
                return
            if k - node.val in seen:
                self.ans = True
                return
            seen.add(node.val)
            dfs(node.left,self.ans)
            dfs(node.right,self.ans)
        dfs(root,self.ans)
        return self.ans