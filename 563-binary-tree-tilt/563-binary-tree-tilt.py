# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def findSum(node):
            temp = 0
            if node is None:
                return temp
            temp += node.val
            temp += findSum(node.left)
            temp += findSum(node.right)
            return temp
                
        def dfs(node):
            if node is None:
                return 0
            node.val = abs(findSum(node.left) - findSum(node.right))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        ans = findSum(root)
        return ans