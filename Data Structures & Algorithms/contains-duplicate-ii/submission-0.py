class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        currentHash = dict()

        for rightPointer in range(0, len(nums)):
            currentValue = nums[rightPointer]
            print(f"Current Value is {currentValue}. Right Pointer is {rightPointer}")
            if currentValue in currentHash and abs(currentHash[currentValue] - rightPointer) <= k:
                return True
            currentHash[currentValue] = rightPointer

        return False
         
