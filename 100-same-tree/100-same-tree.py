# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        def dfs(r1,r2):
            if r1 is None:
                if r2 is None:
                    return
                else:
                    self.flag = False
                    return
            if r2 is None:
                if r1 is None:
                    return
                else:
                    self.flag = False
                    return
            if r1.val != r2.val:
                self.flag = False
                return
            dfs(r1.left,r2.left)
            dfs(r1.right,r2.right)
            return self.flag
        return dfs(p,q)
        
            
            