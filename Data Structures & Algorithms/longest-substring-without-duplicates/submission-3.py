class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or s == '':
            return 0

        leftPointer = 0
        length = 0
        currentSubstring = ''

        for rightPointer in range(0, len(s)):
            currentChar = s[rightPointer]
            if(currentChar in currentSubstring):
                currentSubstring = currentSubstring.split(currentChar)[1]
            currentSubstring += currentChar
            length = max(length, len(currentSubstring))

        return length
