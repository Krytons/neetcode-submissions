class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Brute force O(n)
        return self.bruteForce(nums)

    def bruteForce(self, nums) -> int:
        numset = set()

        for number in nums:
            if number not in numset:
                numset.add(number)
            else:
                return number
        
        return math.nan