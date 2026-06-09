class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        totals, leftPointer = 0, 0
        length = math.nan

        for rightPointer in range(0, len(nums)):
            totals += nums[rightPointer]
            while totals >= target:
                length = min(rightPointer - leftPointer + 1, length)
                totals -= nums[leftPointer]
                leftPointer += 1

        return length if length is not math.nan else 0