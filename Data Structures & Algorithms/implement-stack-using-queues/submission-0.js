class MyStack {
    constructor() {
        this.values = [];
    }

    /**
     * @param {number} x
     * @return {void}
     */
    push(x) {
        this.values.push(x);
    }

    /**
     * @return {number}
     */
    pop() {
        return this.values.pop();
    }

    /**
     * @return {number}
     */
    top() {
        return this.values[this.values.length - 1];
    }

    /**
     * @return {boolean}
     */
    empty() {
        return this.values.length === 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */
