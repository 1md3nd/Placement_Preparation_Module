# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        q = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            q.append(node.val)
            dfs(node.right)
        dfs(root)
        new = TreeNode(q.pop(0))
        head = new
        while q:
            new.right = TreeNode(q.pop(0))
            # new.left = TreeNode(null)
            new = new.right
        return head
    