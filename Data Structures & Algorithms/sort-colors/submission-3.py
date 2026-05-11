def swapPosition(array, origin, destination):
    array[origin], array[destination] = array[destination], array[origin]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        lo = 0
        hi = len(nums) - 1
        mid = 0

        while mid <= hi:
            match nums[mid]:
                case 0:
                    swapPosition(nums, mid, lo)
                    lo += 1
                    mid += 1
                case 1: 
                    mid += 1
                case 2:
                    swapPosition(nums, mid, hi)
                    hi -= 1
