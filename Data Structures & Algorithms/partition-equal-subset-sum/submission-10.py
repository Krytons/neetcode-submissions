class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if (totalSum % 2 == 1):
            return False


        """
        Standard memoization
        """
        # return self.standardMemoization(totalSum/2, nums)

        """
        Knapsack 0/1
        """
        return self.knapsack(totalSum//2, nums)


    def knapsack(self, capacity, nums) -> bool:
        previousLayer = []
        for currentCapacity in range(0, capacity + 1):
            if currentCapacity < nums[0]:
                previousLayer.append(0)
            else:
                previousLayer.append(nums[0])

        currentLayer = [0] * (capacity + 1) 
        for index in range(1, len(nums)):
            currentLayer[0] = 0
            for currentCapacity in range(1, capacity + 1):
                skipSum = previousLayer[currentCapacity]
                includeSum = 0
                newCapacity = currentCapacity - nums[index]
                if newCapacity >= 0:
                    includeSum = nums[index] + previousLayer[newCapacity]
                
                currentLayer[currentCapacity] = max(includeSum, skipSum)
                if currentLayer[currentCapacity] == capacity:
                    return True

            previousLayer, currentLayer = currentLayer, previousLayer

        return False



    def standardMemoization(self, capacity, nums) -> bool:
        cache = {} 
        def partition(index, nums, currentCapacity, cache) -> bool:
            if index >= len(nums):
                return currentCapacity == 0
            if (index, currentCapacity) in cache:
                return cache[(index, currentCapacity)]

            #Skip case:
            cache[(index, currentCapacity)] = partition(index +1, nums, currentCapacity, cache)

            #Take case:
            newCapacity = currentCapacity - nums[index]
            if newCapacity >= 0 and cache[(index, currentCapacity)] != True:
                cache[(index, currentCapacity)] = partition(index +1, nums, newCapacity, cache)

            return cache[(index, currentCapacity)]
        
        return partition(0, nums, capacity, cache)

        

