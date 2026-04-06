# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next

        while f and f.next:
            s = s.next
            f = f.next.next

        
        l2 = s.next 
        s.next = None
        prev = None

        while l2:
            tmp = l2.next
            l2.next = prev 
            prev = l2
            l2 = tmp

        second = prev
        first = head 

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        


