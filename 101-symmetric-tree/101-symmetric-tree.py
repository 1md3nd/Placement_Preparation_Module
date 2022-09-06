# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        while q:
            size = len(q)
            level = []
            for i in range(size):
                head = q.pop(0)
                if head:
                    level.append(head.val)
                    q.append(head.left)
                    q.append(head.right)
                else:
                    level.append("null")
            print(level)
            if level != level[::-1]:
                return False
        return True
                    