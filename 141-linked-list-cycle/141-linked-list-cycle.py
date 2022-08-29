# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # INF = 10 ** 20
        if head == None:
            return False
        # while head.next != None:
        #     if head.val == -INF:
        #         return True
        #     else:
        #         head.val = -INF
        #     head = head.next
        # return False
        #Slow Fast
        slow = head.next
        fast = head
        if head.next == None:
            fast = head.next
        else:
            fast = fast.next.next
        while fast and slow:
            if fast == slow:
                return True
            else:
                slow = slow.next
                fast = fast.next if fast.next is None else fast.next.next
        return False