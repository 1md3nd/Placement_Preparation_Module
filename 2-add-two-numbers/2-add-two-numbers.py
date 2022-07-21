# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pace_val = 1
        a = 0
        while l1:
            a += l1.val*pace_val
            l1 = l1.next
            pace_val = 10*pace_val
        b = 0
        pace_val = 1
        while l2:
            b += l2.val*pace_val
            l2 = l2.next
            pace_val = 10*pace_val
        sum_c = a+b
        new = ListNode()
        new_node = new
        if sum_c < 9:
            current = ListNode(sum_c)
            new_node.next = current

        while sum_c:
            current = ListNode(sum_c%10)
            new_node.next = current
            sum_c = sum_c//10
            new_node = current
        return new.next