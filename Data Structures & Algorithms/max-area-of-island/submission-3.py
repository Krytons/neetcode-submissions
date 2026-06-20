class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0 
        
        maxRow = len(grid) - 1
        maxColumn = len(grid[0]) - 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        maxCount = 0

        def getIslandCount(r, c) -> int:
            stack = [(r, c)]
            visited.add((r, c))
            currentCount = 0
            while stack:
                currentRow, currentColumn = stack.pop()
                currentCount += 1
                for dr, dc in directions:
                    newRow = currentRow + dr
                    newCol = currentColumn + dc
                    if newRow < 0 or newCol < 0 or newRow > maxRow or newCol > maxColumn:
                        continue
                    if (newRow, newCol) in visited or grid[newRow][newCol] == 0:
                        continue
                    visited.add((newRow, newCol))
                    stack.append((newRow, newCol))
            return currentCount

        for currentRow in range(maxRow + 1):
            for currentColumn in range(maxColumn + 1):
                if grid[currentRow][currentColumn] == 1 and (currentRow, currentColumn) not in visited:
                    maxCount = max(maxCount, getIslandCount(currentRow, currentColumn))

        return maxCount
                    
