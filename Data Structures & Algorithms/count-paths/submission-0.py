class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        previousRow = [0] * n
        previousRow[-1] = 1

        for row in range(m-1, -1, -1):
            currentRow = [0] * n
            for column in range(n-1, -1, -1):
                currentRow[column] = previousRow[column] + (currentRow[column + 1] if column + 1 <= n - 1 else 0)
            previousRow = currentRow

        return previousRow[0]