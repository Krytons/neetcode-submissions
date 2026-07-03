class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        current = []
        self.helper(0, current, results, nums, target)
        return results

    def helper(self, index, current, results, nums, target):
        currentSum = sum(current)
        if currentSum == target:
            results.append(current.copy())
            return
        if currentSum > target:
            return

        for subindex in range(index, len(nums)):
            current.append(nums[subindex])
            self.helper(subindex, current, results, nums, target)
            current.pop()