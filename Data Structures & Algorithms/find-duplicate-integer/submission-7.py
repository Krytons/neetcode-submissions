class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Brute force O(n) time and space
        #return self.bruteForce(nums)

        #Pointers approach O(n) time and O(1) space
        return self.pointers(nums)
    
    def pointers(self, nums) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        newSlow = 0
        while True:
            slow = nums[slow]
            newSlow = nums[newSlow]
            if slow == newSlow:
                return slow



    def bruteForce(self, nums) -> int:
        numset = set()

        for number in nums:
            if number not in numset:
                numset.add(number)
            else:
                return number
        
        return -1