# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node,target,seen,total):
            total += node.val
            seen += str(node.val) + " "
            if total == target and node.left is None and node.right is None:
                res.append(seen[0:-1])
                return
            
            if node is None:
                return
            if node.left:
                dfs(node.left,target,seen,total)
            if node.right:
                dfs(node.right,target,seen,total)
        if root is None:
            return []
        dfs(root,targetSum,"",0)
        ans = []
        for x in res:
            ans.append(list(x.split(" ")))
        return ans