class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = {
            0 : 0,
            1 : 0,
            2 : 0
        }

        for element in nums:
            buckets[element] += 1

        counter = 0
        for key in buckets:
            nums[counter : counter + buckets[key]] = [key] * buckets[key]
            counter += buckets[key]
        