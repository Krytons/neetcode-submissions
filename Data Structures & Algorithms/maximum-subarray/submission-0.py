class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return nums[0]

        maxSum = nums[0]
        currentSum = 0

        for number in nums:
            currentSum = max(currentSum, 0)
            currentSum += number
            maxSum = max(maxSum, currentSum)
        
        return maxSum