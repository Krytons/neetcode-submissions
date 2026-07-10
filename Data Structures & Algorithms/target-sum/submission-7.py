class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        currentSum = 0
        return self.backpropagate(0, nums, target, currentSum)

    def backpropagate(self, index, nums, target, currentSum):
        if index == len(nums):
            if currentSum == target:
                return 1
            return 0

        #Choose the addition
        results = 0
        currentSum += nums[index]
        results += self.backpropagate(index + 1, nums, target, currentSum)
        #Choose the subtraction
        currentSum -= (nums[index] * 2) #The multiply is done to undo the summation
        results += self.backpropagate(index + 1, nums, target, currentSum)

        return results