class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)      
        leftSum = 0
        
        for i, num in enumerate(nums):
            # rightSum = total - leftSum - nums[i]
            if leftSum == total - leftSum - num:
                return i
            leftSum += num
        
        return -1