# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        def preorder(node,x,y):
            if node is None:
                return
            dic[y].append((x,node.val))
            preorder(node.left,x+1,y-1)
            preorder(node.right,x+1,y+1)
        preorder(root,0,0)
        res = []
        # print(dic)
        for key,values in sorted(dic.items()):
            values = sorted(values)
            res.append([val[1] for val in values])
        return res