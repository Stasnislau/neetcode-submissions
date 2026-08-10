# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryOn = 0
        A = l1 # bigger
        B = l2 # smaller
        prevA = None
        while A and B:
            res = A.val + B.val + carryOn 
            if res > 9:
                A.val = res - 10
                carryOn = 1
            else:
                A.val = res
                carryOn = 0
            prevA = A
            A = A.next
            B = B.next
        if not A and B:
            prevA.next = B
            A = B

        if carryOn == 0:
            return l1
        else:
            while carryOn == 1:
                if not A:
                    A = ListNode(1)
                    prevA.next = A
                    carryOn = 0
                else:
                    res = A.val + carryOn
                    if res > 9:
                        A.val = 0
                        carryOn = 1
                    else:
                        A.val = res
                        carryOn = 0
                prevA = A
                A = A.next
                
        return l1

        
        

