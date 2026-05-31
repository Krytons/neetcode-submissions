class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxPosition = len(nums) - 1
        if maxPosition == 0:
            return nums[0]

        memory = {}

        def bestPath(position : int):
            if position > maxPosition:
                return 0
            if position in memory:
                return memory[position]

            #Rob or skip?
            result = max(nums[position] + bestPath(position+2), bestPath(position+1))
            memory[position] = result
            return result

        return bestPath(0)