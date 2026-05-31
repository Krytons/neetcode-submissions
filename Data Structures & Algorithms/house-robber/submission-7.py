class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        #Formula - Result[i] = max(Nums[i] + Result[i - 2], Result[i - 1]) = max(Rob current, Skipped current)
        previous2 = nums[0]
        previous1 = max(nums[0], nums[1])
        for position in range(2, len(nums)):
            result = max(nums[position] + previous2, previous1)
            previous2, previous1 = previous1, result

        return max(previous2, previous1)
