class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = [(0, [])]

        while stack:
            idx, path = stack.pop()
            result.append(path)

            for i in range(idx, len(nums)):
                stack.append((i + 1, path + [nums[i]]))

        return result

