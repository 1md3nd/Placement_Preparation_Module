# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, node: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(root,temp):
            if root.left is None and root.right is None:
                temp += str(root.val)
                res.append(temp)
                # temp = ""
                return res
            if root:
                temp += str(root.val) + "->"
            if root.left:
                # temp+= str(root.val)
                dfs(root.left,temp)
            if root.right:
                # temp+= str(root.val)
                dfs(root.right,temp)
                # temp = ""
            return res
        res = dfs(node,"")
        # ans = []
        # # print(res)
        # for x in res:
        #     ans.append("->".join(x))
        return res