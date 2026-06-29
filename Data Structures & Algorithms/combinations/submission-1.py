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

        #Version 2^n
        #current.append(index)
        #self.computeSubset(index + 1, current, result, n, k)
        #current.pop()
        #self.computeSubset(index + 1, current, result, n, k)

        #Version C(n,k)
        for subindex in range (index, n+1):
            current.append(subindex)
            self.computeSubset(subindex + 1, current, result, n, k)
            current.pop()