class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #result = []
        #stack = [(0, [])]

        #while stack:
        #    idx, path = stack.pop()
        #   result.append(path)
        # 
        #    for i in range(idx, len(nums)):
        #        stack.append((i + 1, path + [nums[i]]))

        #return result

        currentStack, result = [], []
        self.computeSubset(0, nums, currentStack, result)
        return result

    def computeSubset(self, index, nums, currentStack, result):
        if index >= len(nums):
            result.append(currentStack.copy())
            return
    
        currentStack.append(nums[index])
        self.computeSubset(index + 1, nums, currentStack, result)
        currentStack.pop()
        self.computeSubset(index + 1, nums, currentStack, result)