# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def check(dic):
            odd = 0
            for k,val in dic.items():
                if val % 2 == 0:
                    continue
                else:
                    odd +=1
            if odd > 1:
                return False
            return True
        self.count = 0
        def dfs(node,dic):
            if node is None:
                return
            if node.val not in dic:
                dic[node.val] = 1
            else:
                dic[node.val] +=1
            if node.left is None and node.right is None:
                if check(dic):
                    self.count +=1
                dic[node.val] -=1
                return
            dfs(node.left,dic)
            dfs(node.right,dic)
            dic[node.val] -=1
        dfs(root,{})
        return self.count