// class Node {
//   constructor(val, next = null, random = null) {
//       this.val = val;
//       this.next = next;
//       this.random = random;
//   }
// }

class Solution {
    /**
     * @param {Node} head
     * @return {Node}
     */
    copyRandomList(head) {
        let newHead = new Node();
        const map = new Map();
        let node = head;
        let newNode = newHead;
        while (node){
            newNode.next = new Node(node.val);
            map.set(node, newNode.next);
            node = node.next;
            newNode = newNode.next;
        }
        newHead = newHead.next;
        newNode = newHead;
        node = head;
        while (node){
            newNode.random = map.get(node.random);
            node = node.next;
            newNode = newNode.next;
        }
        return newHead;
    }
}
