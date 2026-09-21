# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(0, head)
        fast = head
        slow = dummy
        res = 0
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
            slow = slow.next
        print(fast, slow.val)
        twin = None
        prev = slow
        slow = slow.next
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        curr = head
        twin = prev
        while twin:
            res = max(res, curr.val + twin.val)
            curr = curr.next
            if curr == twin:
                break
            twin = twin.next
        return res