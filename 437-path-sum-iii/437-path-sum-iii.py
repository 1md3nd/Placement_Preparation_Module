# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def test(node,val):
            if node is None:
                return
            if node.val == val:
                self.count +=1
            test(node.left,val - node.val)
            test(node.right,val - node.val )
            return
        def dfs(node,val):
            if node is None:
                return
            test(node,val)
            dfs(node.left,val)
            dfs(node.right,val)
            return
        dfs(root,targetSum)
        return self.count
            