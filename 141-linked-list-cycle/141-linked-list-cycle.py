# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        INF = 10 ** 20
        if head == None:
            return False
        while head.next != None:
            if head.val == -INF:
                return True
            else:
                head.val = -INF
            head = head.next
        return False