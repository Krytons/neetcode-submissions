class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for number in nums:
            currentCalculus = []
            for permutation in result:
                for index in range(len(permutation) + 1):
                    copy = permutation.copy()
                    copy.insert(index, number)
                    currentCalculus.append(copy)
            result = currentCalculus
        
        return result
        