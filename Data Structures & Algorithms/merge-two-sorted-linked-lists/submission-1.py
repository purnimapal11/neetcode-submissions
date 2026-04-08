# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        dummy = ListNode(0)
        ans = dummy

        while a and b:
            if a.val > b.val:
                dummy.next = b
                b = b.next
            else:
                dummy.next = a
                a = a.next
            dummy = dummy.next
        
        if a:
            dummy.next = a
        if b:
            dummy.next = b

        return ans.next