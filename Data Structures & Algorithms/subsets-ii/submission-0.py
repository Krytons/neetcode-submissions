class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        result, current = [], []
        nums.sort()
        self.helper(0, nums, current, result)
        return result

    def helper(self, i, nums, current, result):
        if i >= len(nums):
            result.append(current.copy())
            return
        
        current.append(nums[i])
        self.helper(i + 1, nums, current, result)
        current.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.helper(i + 1, nums, current, result)