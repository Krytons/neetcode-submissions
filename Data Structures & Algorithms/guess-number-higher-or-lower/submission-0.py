# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        myguess = 0
        high = 2147483647
        result = 1
        while result != 0:
            myguess = low + ((high-low) // 2)
            result = guess(myguess)
            print(f"Result is {result}")
            match result:
                case 0:
                   return myguess
                case 1:
                    low = myguess + 1
                case -1:
                    high = myguess - 1

        
