class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        #Start with first char
        maxSequence = 1
        currentSequence = 1
        maxChar = s[0]
        charMap = {}
        charMap[maxChar] = 1
        delta = 0
        startWindow, endWindow = 0,1

        while endWindow < len(s):
            #Get new char
            currentChar = s[endWindow]
            if currentChar not in charMap:
                charMap[currentChar] = 1
            else:
                charMap[currentChar] += 1
                maxChar = currentChar if charMap[currentChar] >= charMap[maxChar] else maxChar

            #Evaluate delta increase
            currentSequence += 1
            delta = currentSequence - charMap[maxChar]

            #Evaluate start window move by looking at delta
            if delta > k:
                removingChar = s[startWindow]
                charMap[removingChar] -= 1
                currentSequence -= 1
                startWindow += 1

            #Move the window forward
            maxSequence = max(maxSequence, currentSequence)
            endWindow += 1
        
        return maxSequence


