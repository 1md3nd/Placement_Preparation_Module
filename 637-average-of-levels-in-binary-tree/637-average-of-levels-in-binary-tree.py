# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = []
        queue.append(root)
        while queue:
            level = 0
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)
                level += curr.val
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            res.append(level/size)
        return res
            