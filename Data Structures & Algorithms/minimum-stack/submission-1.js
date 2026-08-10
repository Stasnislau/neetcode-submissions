class MinStack {
    minStack;
    stack;
    constructor() {
        this.stack = new Array();
        this.minStack = new Array();
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);
        val = Math.min(this.minStack.length === 0 ? val : this.minStack[this.minStack.length - 1], val)
        console.log(val, this.minStack)
        this.minStack.push(val);
    }

    /**
     * @return {void}
     */
    pop() {
        const value = this.stack.pop()
        this.minStack.pop();
        return value;
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length - 1]
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minStack[this.minStack.length - 1]
    }
}
