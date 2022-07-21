# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        root = temp = head
        count = 0
        while head:
            head = head.next
            count +=1
        if count == n: 
            return root.next
        get = count - n - 1
        while get > 0 and temp:
            temp = temp.next
            get -= 1
        temp.next = temp.next.next
        return root
            