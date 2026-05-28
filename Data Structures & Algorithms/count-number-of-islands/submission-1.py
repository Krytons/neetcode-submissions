class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCounter = 0
        if not grid:
            return islandCounter

        maxRow = len(grid) -1
        maxColumn = len(grid[0]) -1

        for currentRow in range (0, maxRow + 1):
            for currentColumn in range (0, maxColumn + 1):
                currentValue = grid[currentRow][currentColumn]
                if currentValue == '0':
                    grid[currentRow][currentColumn] = '2'
                    continue
                elif currentValue == '2':
                    continue
                else:
                    islandCounter += 1
                    stack = [(currentRow, currentColumn)]
                    while stack:
                        stackRow, stackColumn = stack[-1]
                        grid[stackRow][stackColumn] = '2'
                        
                        #TOP Direction
                        if (stackRow - 1) >= 0 and grid[stackRow - 1][stackColumn] == '1':
                            stack.append((stackRow - 1, stackColumn))
                            continue;

                        #BOTTOM Direction
                        if (stackRow + 1) <= maxRow and grid[stackRow + 1][stackColumn] == '1':
                            stack.append((stackRow + 1, stackColumn))
                            continue;

                        #LEFT Direction
                        if (stackColumn - 1) >= 0 and grid[stackRow][stackColumn - 1] == '1':
                            stack.append((stackRow, stackColumn -1))
                            continue;

                        #RIGHT Direction
                        if (stackColumn + 1) <= maxColumn and grid[stackRow][stackColumn + 1] == '1':
                            stack.append((stackRow, stackColumn +1))
                            continue;
                            
                        #Remove from stack
                        stack.pop()

        return islandCounter
            