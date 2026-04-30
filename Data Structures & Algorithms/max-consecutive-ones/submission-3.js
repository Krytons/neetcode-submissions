class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let maxConsecutives = 0;
        let actualConsecutives = 0;
        nums.forEach(function(element, index){
            let isOne = element === 1;
            if (isOne)
                actualConsecutives++;
            if(!isOne || index === (nums.length -1)) {
                maxConsecutives = maxConsecutives > actualConsecutives ? maxConsecutives : actualConsecutives;
                actualConsecutives = 0;
            }
        });

        return maxConsecutives;
    }
}

let currentSolution = new Solution();
console.log(currentSolution.findMaxConsecutiveOnes([1,1,0,1,1,1]))