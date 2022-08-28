class Solution:
    def isValidBST(self, root: Optional[TreeNode], left = float('-inf'), right = float('inf')) -> bool:
        if not root:
            return True
            
        if left >= root.val or root.val >= right:
            return False
            
        return self.isValidBST(root.left, left, root.val) and self.isValidBST(root.right, root.val, right)