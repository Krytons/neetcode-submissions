class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0 
        
        visited = set()
        visited.add((0,0))
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        stack = [(0,0)]
        currentIsland = []
        maxCount = 0
        currentCount = 0

        maxRow = len(grid) - 1  
        maxColumn = len(grid[0]) -1 

        while stack and len(stack) > 0:
            currentRow, currentColumn = stack.pop()
            currentValue = grid[currentRow][currentColumn]

            #Found island logic
            if currentValue == 1:
                currentIsland.append((currentRow, currentColumn))
                visited.add((currentRow, currentColumn))
                while currentIsland and len(currentIsland) > 0:
                    islandRow, islandColumn = currentIsland.pop()
                    islandValue = grid[islandRow][islandColumn]

                    currentCount += 1
                    print(f"New count is {currentCount}. Processed {islandRow}{islandColumn}")
                    for dr, dc in directions:
                        newRow = dr + islandRow
                        newCol = dc + islandColumn
                        print(f"Evaluating {newRow}{islandColumn}")
                        if min(newRow, newCol) < 0 or newRow > maxRow or newCol > maxColumn or (newRow, newCol) in visited:
                            continue
                        if grid[newRow][newCol] == 0:
                            stack.append((newRow, newCol))
                        else:
                            currentIsland.append((newRow, newCol))
                        visited.add((newRow, newCol))

                maxCount = max(maxCount, currentCount)
                currentCount = 0

            
            #Explore more
            for dr, dc in directions:
                newRow = dr + currentRow
                newCol = dc + currentColumn
                if min(newRow, newCol) < 0 or newRow > maxRow or newCol > maxColumn or (newRow, newCol) in visited:
                    continue
                stack.append((newRow, newCol))
                if grid[newRow][newCol] == 0:
                    visited.add((newRow, newCol))
                    
        return maxCount
                    
