class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pi,pj=0,1
        maxLength = len(numbers) - 1

        while True:
            vi = numbers[pi]
            vj = numbers[pj]
            currentSum = vi + vj

            if currentSum < target:
                if pj < maxLength:
                    pj += 1
                else:
                    pi += 1
            elif currentSum == target:
                return [pi+1, pj+1]
            else:
                pj -= 1
                maxLength = pj
 
