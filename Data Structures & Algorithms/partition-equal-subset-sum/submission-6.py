class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if (totalSum % 2 == 1):
            return False

        capacity = totalSum/2
        cache = {} 
    
        def partition(index, nums, currentCapacity, cache) -> bool:
            if index >= len(nums):
                print(f"currentCapacity {currentCapacity}, {currentCapacity == 0}")
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


        

