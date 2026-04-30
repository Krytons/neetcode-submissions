class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let currentSet = new Set();
        for (let i = 0; i < nums.length; i++){
            if(currentSet.has(nums[i]))
                return true;
            else
                currentSet.add(nums[i])
        }
        return false;
    }
}
