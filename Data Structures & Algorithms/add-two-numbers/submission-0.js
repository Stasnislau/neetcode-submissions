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
     * @param {ListNode} l1
     * @param {ListNode} l2
     * @return {ListNode}
     */
    addTwoNumbers(l1, l2) {
        let l1Node = l1;
        let l2Node = l2
        let carryOn = 0;
        let l1Prev = null;
        while (l1Node && l2Node) {
            if (l1Node.val + l2Node.val + carryOn < 10) {
                l1Node.val = l1Node.val + l2Node.val + carryOn
                carryOn = 0;
            }
            else {
                l1Node.val = (l1Node.val + l2Node.val + carryOn) % 10
                carryOn = 1;
            }
            l1Prev = l1Node;
            l1Node = l1Node.next;
            l2Node = l2Node.next;
        }
        let finalList = l1Node || l2Node;
        while (finalList) {
            if (carryOn) {
                if (finalList.val + 1 === 10) {
                    carryOn = 1;
                    finalList.val = 0;
                } else {
                    carryOn = 0;
                    finalList.val = finalList.val + 1;
                }
            }
            l1Prev.next = finalList;
            finalList = finalList.next;
            l1Prev = l1Prev.next
        }
        if (carryOn) {
            l1Prev.next = l2;
            l2.val = 1;
            l2.next = null;
        }
        return l1;
    }
}
