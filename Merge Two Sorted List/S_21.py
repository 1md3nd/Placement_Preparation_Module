# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        new_li = temp
        
        while list1 and list2:
            if list1.val < list2.val:
                new_li.next = list1
                list1 = list1.next
            else:
                new_li.next = list2
                list2 = list2.next
            new_li = new_li.next
        if list1:
            new_li.next = list1    
        if list2:
            new_li.next = list2
        return temp.next