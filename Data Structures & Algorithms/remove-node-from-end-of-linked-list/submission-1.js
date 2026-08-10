/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {
        let fast = head;
        let i = 0;
        while (i < n) {
            fast = fast.next;
            i++;
        }
        let node = head;
        let prev = null;
        while (fast) {
            fast = fast.next;
            prev = node;
            node = node.next;
        }
        if (!prev)
            return head.next;
        prev.next = node.next
        node.next = null;
        return head;
    }
}
