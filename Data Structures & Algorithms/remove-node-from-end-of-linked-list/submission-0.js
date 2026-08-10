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
        let node = head;
        let totalLength = 0;
        while (node) {
            totalLength++;
            node = node.next;
        }
        const nodeToBeRemoved = totalLength - n;
        if (nodeToBeRemoved === 0)
            return head.next;
        let prev = null;
        node = head;
        let i = 0;
        console.log(totalLength, n, nodeToBeRemoved)
        while (i < nodeToBeRemoved) {
            prev = node;
            node = node.next;
            i++
        }
        prev.next = node.next;
        node.next = null
        return head;
    }
}
