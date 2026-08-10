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
     * @return {boolean}
     */
    hasCycle(head) {
        if (!head)
            return false;
        let fast = head.next;
        let slow = head;

        while (fast !== null && fast !== slow) {
            slow = slow.next;
            if (!fast.next)
                return false;
            fast = fast.next.next
        }
        return fast === slow
    }
}
