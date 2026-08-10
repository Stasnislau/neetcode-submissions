# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = head
        count = 0
        while counter:
            count += 1
            counter = counter.next
        curr = head
        toDeleteCount = count - n
        if count == 1:
            return None
        if toDeleteCount == 0:
            return head.next
        while toDeleteCount != 1:
            toDeleteCount -= 1
            curr = curr.next
            if curr == head:
                head = head.next
        curr.next = curr.next.next
        return head