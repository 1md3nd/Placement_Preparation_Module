# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = []
        q.append(root)
        res = 0
        head = root
        while q:
            size = len(q)
            for _ in range(size):
                head = q.pop(0)
                if head.val >= low and head.val <= high:
                    # print(head.val)
                    res+=head.val
                if head.left and head.val > low: 
                    q.append(head.left)
                if head.right and head.val < high:
                    q.append(head.right)
        return res            