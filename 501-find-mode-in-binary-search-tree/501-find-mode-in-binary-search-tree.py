# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            dic[root.val] = 1 + dic.get(root.val,0)
            root = root.right
        ans = []
        maxx = max(dic.values())
        for x in dic.keys():
            if dic[x] == maxx:
                ans.append(x)
        return ans