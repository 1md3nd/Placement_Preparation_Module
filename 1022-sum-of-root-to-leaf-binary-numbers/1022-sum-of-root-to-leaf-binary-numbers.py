# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(root,bn):
            if not root.left and not root.right:
                res.append(bn+str(root.val))
                return
            if root.left:
                dfs(root.left,bn+str(root.val))
            if root.right:
                dfs(root.right,bn+str(root.val))
        dfs(root,"")
        print(res)
        final = 0
        for x in res:
            i = len(x) - 1 
            temp = 0
            for k in x:
                temp += int(k) * (2 ** i)
                i -=1
            final += temp
        return final