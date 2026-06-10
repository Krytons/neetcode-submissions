class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.postfix = []
        currentSum = 0
        for number in nums:
            currentSum += number
            self.postfix.append(currentSum)
        print(f"{self.postfix}")

    def sumRange(self, left: int, right: int) -> int:
        if left < 0 or right > len(self.nums) or right < left:
            return 0
        
        currentSum = self.postfix[right]
        previousSum = self.postfix[left - 1] if left - 1 >= 0 else 0
        print(f"{currentSum} - {previousSum}")
        return currentSum - previousSum



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)