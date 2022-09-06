# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = TreeNode(-1,root)
        def dfs(node):
            if node is None:
                return False
            flag = False
            if node.val == 1:
                flag = True
            if not dfs(node.left):
                node.left = None
            else:
                flag = True
            if not dfs(node.right):
                node.right = None
            else:
                flag = True
            return flag 
        
        dfs(head)
        # print(root)
        return head.left
            