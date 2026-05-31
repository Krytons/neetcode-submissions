class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxPosition = len(nums) - 1
        if maxPosition == 0:
            return nums[0]

        memory = {}

        def bestPath(position):
            if position + 1 >= maxPosition:
                return nums[position]

            currentMax = 0
            for index in range(position + 2, maxPosition + 1):
                currentPath = memory[index] if index in memory else bestPath(index)
                if currentPath > currentMax:
                    currentMax = currentPath

            if position not in memory:
                memory[position] = nums[position] + currentMax
            return nums[position] + currentMax

        return max(bestPath(0), bestPath(1))