# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        nodesAhead = 0
        prevSegment = None
        curr = head
        nodeAhead = dummy
        dummy.next = head

        if not head:
            return None
        
        while curr:
            nodesAheadCount = 0
            first = nodeAhead.next
            for _ in range(k):
                if nodeAhead:
                    nodesAheadCount += 1
                    nodeAhead = nodeAhead.next
                
                
                if nodesAheadCount == k and nodeAhead:
                    if head == curr:
                        dummy.next = nodeAhead
                    nextSegment = nodeAhead.next
                    
                    prev = nextSegment
                    # print(curr.val, 'curr', prevSegment.val if prevSegment else '')

                    while curr:
                        print(prev.val if prev else 'nothing', 'prev')
                        temp = curr.next
                        curr.next = prev
                        prev = curr
                        curr = temp
                        if prev == nodeAhead:
                            print('break', curr.val if curr else "NONE", prev.val if prev else "NONE")
                            break
                    test = dummy.next
                
                    while test:
                        print(test.val, 'test')
                        test = test.next
                    print('end')
                    # print('reverting', curr.val, nextSegment.val if nextSegment else '')
                    
                    if prevSegment:
                        prevSegment.next = prev
                    if curr: 
                        prevSegment = first
                    curr = nextSegment
                    nodeAhead = first                  

            if not nodeAhead or not curr:
                return dummy.next
                
        return dummy.next