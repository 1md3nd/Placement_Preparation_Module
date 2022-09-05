# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        fix = root.val
        q = [root]
        while q:
            size = len(q)
            for i in range(size):
                head = q.pop(0)
                if head.val == fix:
                    if head.left:
                        q.append(head.left)
                    if head.right:
                        q.append(head.right)
                else:
                    return False
        return True