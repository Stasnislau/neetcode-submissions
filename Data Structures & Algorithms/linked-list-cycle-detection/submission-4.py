# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        curr = head
        fast = head.next
        while curr and fast:
            print(curr.val, fast.val)
            if curr == fast and curr != None:
                return True
            curr = curr.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = fast.next
        return False