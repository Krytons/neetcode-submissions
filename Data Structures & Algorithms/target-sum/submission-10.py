class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mappings = [defaultdict(int) for element in range(len(nums)+1)]
        mappings[0][0] = 1 

        for index in range(0, len(nums)):
            for summation, ways in mappings[index].items():
                mappings[index + 1][summation + nums[index]] += ways 
                mappings[index + 1][summation - nums[index]] += ways

        return mappings[len(nums)][target]


        """ Backtraging + Memoize Solution
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
        """