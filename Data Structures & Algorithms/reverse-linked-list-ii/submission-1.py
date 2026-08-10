# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        prev = None
        for _ in range(1, left):
            prev = curr
            curr = curr.next
        first_prev = prev
        first = curr
        for _ in range(left, right + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        first.next = curr
        if first_prev:
            first_prev.next = prev
        return head if first_prev else prev
        
