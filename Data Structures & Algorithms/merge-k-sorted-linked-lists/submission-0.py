# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i + 1 < len(lists) else None
                newHead = ListNode()
                if not list1 or not list2:
                    newHead.next = list1 or list2
                    mergedLists.append(newHead.next)
                    continue
                
                curr = newHead
                while list1 and list2:
                    if list1.val > list2.val:
                        curr.next = list2
                        list2 = list2.next
                    else:
                        curr.next = list1
                        list1 = list1.next
                    curr = curr.next
                curr.next = list1 or list2
                mergedLists.append(newHead.next)
            print('lists', len(lists), len(mergedLists))
            lists = mergedLists
        return lists[0]