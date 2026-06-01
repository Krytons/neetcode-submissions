class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        #For better readability
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        previousRow = [0] * columns
        previousRow[-1] = 1
        for row in range(rows-1, -1, -1):
            #Current row is given by the grid itself
            for column in range(columns-1, -1, -1):
                if obstacleGrid[row][column] == 1:
                    obstacleGrid[row][column] = 0
                else:
                    obstacleGrid[row][column] = previousRow[column] + (obstacleGrid[row][column + 1] if column + 1 <= columns - 1 else 0)
            previousRow = obstacleGrid[row]

        return previousRow[0]