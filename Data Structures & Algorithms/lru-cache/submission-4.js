class Node {
    next = null;
    prev = null;
    value = 0;
    key = 0;
    length = 0;
    constructor(key, val) {
        this.value = val;
        this.key = key;
    }
}

class LRUCache {
    /**
     * @param {number} capacity
     */
    constructor(capacity) {
        this.max = capacity;
        this.nodesMap = new Map();
        this.tail = null;
        this.head = null;
        this.length = 0;
        this.head = null;
    }

    /**
     * @param {number} key
     * @return {number}
     */
    append(node) {
        if (this.head) {
            this.head.prev = node;
            node.next = this.head;
            this.head = node;
        } else {
            this.head = node;
            this.tail = node;
        }
        this.nodesMap.set(node.key, node)
        this.length++;
    }

    remove(node) {
        if (this.length === 1) {
            this.head = null;
            this.tail = null;
        } else if (node === this.head) {
            this.head = this.head.next;
            this.head.prev = null;
        } else if (node === this.tail) {
            this.tail = this.tail.prev;
            this.tail.next = null;
        }
        else {
            node.next.prev = node.prev;
            node.prev.next = node.next;
            node.next = null;
            node.prev = null;
        }
        this.length--;
        this.nodesMap.delete(node.key)
    }

    get(key) {
        const node = this.nodesMap.get(key);
        if (node) {
            const newNode = new Node(node.key, node.value)
            this.remove(node);
            this.append(newNode);
        }
        return node?.value ? node.value : -1
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        const oldNode = this.nodesMap.get(key);
        if (oldNode) {
            this.remove(oldNode);
        }
        const node = new Node(key, value);
        if (this.length === this.max) {
            this.remove(this.tail);
        }
        this.append(node);
        // console.log("set", key, node)
    }
}
