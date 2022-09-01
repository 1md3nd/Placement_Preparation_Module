# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxx = root.val
        count = 0
        def dfs(node,maxx):
            nonlocal count
            if node is None:
                return
            if node.val >= maxx:
                count +=1
                maxx = node.val
            # if node.val < maxx:
            #     continue
            dfs(node.left,maxx)
            dfs(node.right,maxx)
            return
        dfs(root,maxx)
        return count
        