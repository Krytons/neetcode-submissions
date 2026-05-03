class MinStack {
    constructor() {
        this.values = [];
        this.minStack = [];
    }


    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        let currentMin = this.getMin();
        this.values.push(val);
        if(currentMin === null || currentMin >= val)
            this.minStack.push(val);
    }

    /**
     * @return {void}
     */
    pop() {
        let removedValue = this.values.pop();
        let currentMin = this.getMin();
        if (removedValue === currentMin){
            this.minStack.pop();
        }
    }

    /**
     * @return {number}
     */
    top() {
        return this.values[this.values.length - 1];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minStack.length > 0 ? this.minStack[this.minStack.length - 1] : null;
    }
}
