class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        current, result = [], []
        self.computeSubset(1, current, result, n, k)
        return result

    def computeSubset(self, index, current, result, n, k):
        if len(current) == k:
            result.append(current.copy())
            return
        if index > n:
            return
    
        current.append(index)
        self.computeSubset(index + 1, current, result, n, k)
        current.pop()
        self.computeSubset(index + 1, current, result, n, k)