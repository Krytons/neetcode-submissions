class Solution:
    def isPalindrome(self, s: str) -> bool:     
        rightPointer, leftPointer = len(s) - 1, 0

        while leftPointer < rightPointer:
            while leftPointer < rightPointer and not s[leftPointer].isalnum():
                leftPointer += 1
            while leftPointer < rightPointer and not s[rightPointer].isalnum():
                rightPointer -= 1

            if (s[leftPointer].lower() == s[rightPointer].lower()):
                leftPointer += 1
                rightPointer -= 1
            else:
                return False

        return True