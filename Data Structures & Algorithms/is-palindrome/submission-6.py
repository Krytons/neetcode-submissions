class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = s.strip()
        if s == "":
            return True

        rightPointer, leftPointer = len(s) - 1, 0

        while leftPointer < rightPointer:
            if not s[leftPointer].isalnum():
                leftPointer += 1
                continue
            elif not s[rightPointer].isalnum():
                rightPointer -= 1
                continue

            if (s[leftPointer].lower() == s[rightPointer].lower()):
                leftPointer += 1
                rightPointer -= 1
            else:
                return False

        return True