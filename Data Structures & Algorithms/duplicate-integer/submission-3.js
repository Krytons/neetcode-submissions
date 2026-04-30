class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let uniqueNumbers = new Set();
        for (let i = 0; i < nums.length; i++){
            let number = nums[i];
            if (!uniqueNumbers.has(number))
                uniqueNumbers.add(number)
            else 
                return true;
        }
        return false;
    }
}


let solution = new Solution();
let nums = [1,2,2,3,4,5,5];
console.log(solution.hasDuplicate(nums));
