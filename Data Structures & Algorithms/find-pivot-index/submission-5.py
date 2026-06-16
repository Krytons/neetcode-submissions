class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        length = len(nums)
        if length == 1:
            return 0
        
        #Build left prefix sum array
        leftSum = []
        currentSum = 0
        for number in nums:
            currentSum += number
            leftSum.append(currentSum)


        for index in range(0, length):
            currentLeft = leftSum[index] - nums[index]
            currentRight = leftSum[length - 1] - leftSum[index]

            if currentLeft == currentRight:
                return index
        return -1