# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        head = root
        stack = []
        while head or stack:
            while head:
                res.append(head.val)
                stack.append(head)
                head = head.left
            head = stack.pop()
            head = head.right
            
        return res
        