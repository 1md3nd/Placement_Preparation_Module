# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recursion(node,left,right):
            if left <= node.val <= right:
                return node
            if right <= node.val:
                return recursion(node.left,left,right)
            return recursion(node.right,left,right)
        return recursion(root,min(p.val,q.val),max(p.val,q.val))