# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, Ahead: ListNode, Bhead: ListNode) -> Optional[ListNode]:
        A = 0
        B = 0
        headA = Ahead
        headB = Bhead
        while headA:
            A +=1
            headA = headA.next
        while headB:
            B +=1
            headB = headB.next
        headA = Ahead
        headB = Bhead
        if A > B:
            dif = A - B
            while dif > 0:
                headA = headA.next
                dif -=1
        else:
            dif = B - A
            while dif > 0:
                headB = headB.next
                dif -=1
        while headA != headB:
            headA= headA.next
            headB= headB.next
        if headA is None and headB is None:
            return
        else: return headA