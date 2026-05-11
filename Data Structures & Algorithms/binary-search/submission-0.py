class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        mid = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + math.floor((hi - lo)/2)
            if (nums[mid] == target):
                return mid
            elif (nums[mid] < target):
                lo = mid + 1
            else:
                hi = mid - 1
            
        return lo if nums[lo] == target else -1