class Solution {
    mergeDeleteSort(nums,val){
        if(nums.length === 0 || (nums.length === 1 && nums[0] === val))
            return [];
        else if (nums.length === 1)
            return nums;

        var l = nums.length;
        var mid = Math.floor(l/2);

        var left = this.mergeDeleteSort(nums.splice(0,mid), val);
        var right = this.mergeDeleteSort(nums, val);

        return this.merge(left, right);
    }

    merge(left, right) {
        const result = [];
        let i = 0, j = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) 
                result.push(left[i++]);
            else                      
                result.push(right[j++]);
        }
        while (i < left.length)  
            result.push(left[i++]);
        while (j < right.length) 
            result.push(right[j++]);

        return result;
    }

    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums, val) {
    const filtered = this.mergeDeleteSort(nums.slice(), val); // slice per non mutare subito
    for (let i = 0; i < filtered.length; i++) {
        nums[i] = filtered[i];
    }
    return filtered.length;
}
}
