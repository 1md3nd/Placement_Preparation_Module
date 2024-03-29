# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first, second = head, head
        while first and first.next:
            first = first.next.next
            second = second.next
        
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
        