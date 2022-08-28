# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def solve(left,right):
            nonlocal nums
            if right < left:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = solve(left,mid-1)
            node.right = solve(mid+1,right)
            return node
        return solve(0,len(nums)-1)