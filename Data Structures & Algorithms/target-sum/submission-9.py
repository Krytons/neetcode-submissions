class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        currentSum = 0
        cache = {}
    
        def backtracking(index, nums, target, currentSum):
            if index == len(nums):
                return 1 if currentSum == target else 0
            elif (index, currentSum) in cache:
                return cache[(index, currentSum)]


            #Choose the addition
            results = backtracking(index + 1, nums, target, currentSum + nums[index]) + backtracking(index + 1, nums, target, currentSum - nums[index])
            cache[(index, currentSum)] = results
            return results

        return backtracking(0, nums, target, currentSum)