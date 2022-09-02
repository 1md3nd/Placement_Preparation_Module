# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        q = []
        new = TreeNode()
        head = new
        def dfs(node):
            nonlocal new
            if node is None:
                return
            dfs(node.left)
            new.right = TreeNode(node.val)
            new = new.right
            dfs(node.right)
        dfs(root)
        # new = TreeNode(q.pop(0))
        # head = new
        # while q:
        #     new.right = TreeNode(q.pop(0))
        #     new = new.right
        # return head
        return head.right
    