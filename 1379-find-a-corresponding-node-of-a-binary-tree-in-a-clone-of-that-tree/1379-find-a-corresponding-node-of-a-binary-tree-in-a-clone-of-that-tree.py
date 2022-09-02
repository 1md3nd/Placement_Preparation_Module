# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # head = cloned
        "BFS"
        # q = []
        # q.append(head)
        # while q:
        #     size = len(q)
        #     for _ in range(size):
        #         head = q.pop(0)
        #         if head.val == target.val:
        #             return head
        #         if head.left:
        #             q.append(head.left)
        #         if head.right:
        #             q.append(head.right)
        "DFS"
        res = TreeNode(0)
        def dfs(head,target):
            nonlocal res
            # if head is None:
            #     return
            # print(head.val)
            if head.val == target.val:
                res = head
                return
            if head.left:
                dfs(head.left,target)
            if head.right:
                dfs(head.right,target)
        dfs(cloned,target)
        return res