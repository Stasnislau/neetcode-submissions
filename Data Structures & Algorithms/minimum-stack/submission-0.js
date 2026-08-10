class MinStack {
    minValue;
    stack;
    constructor() {
        this.stack = new Array();
        this.minValue = Infinity;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.stack.push(val);
        if (val < this.minValue)
            this.minValue = val;
    }

    /**
     * @return {void}
     */
    pop() {
        const value = this.stack.pop()
        if (value === this.minValue)
            this.minValue = this.stack.reduce((min, value) => {
                if (min > value)
                    return value;
                return min
            }, Infinity)
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
        return this.minValue;
    }
}
