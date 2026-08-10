# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        slow = head
        fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        newList = slow.next
        slow.next = None
        fast = newList
        prev = None
        while fast:
            temp = fast.next
            fast.next = prev
            prev = fast
            fast = temp
        fast = prev
        slow = head
        while fast and slow:
            temp = fast.next
            temp2 = slow.next
            fast.next = slow.next
            slow.next = fast
            slow = fast.next
            fast = temp
            


            




            

