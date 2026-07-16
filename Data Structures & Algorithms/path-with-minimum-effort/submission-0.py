import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        
        #Useful constants
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        maxRow = len(heights) - 1
        maxCol = len(heights[0]) - 1

        #Min heap setup
        minHeap = []
        heapq.heappush(minHeap, (0, (0,0))) #Cost - Coordinates
        maxCost = 0
        visited = set()

        #Execution core
        while (maxRow, maxCol) not in visited:
            cost, coordinates = heapq.heappop(minHeap)
            (row, col) = coordinates
            maxCost = max(cost, maxCost)
            visited.add((row, col))

            if row == maxRow and col == maxCol:
                break;
            for dirRow, dirCol in directions:
                newRow = row + dirRow
                newCol = col + dirCol
                if (newRow, newCol) not in visited and newRow >= 0 and newCol >= 0 and newRow <= maxRow and newCol <= maxCol:
                    newCost = abs(heights[newRow][newCol] - heights[row][col])
                    heapq.heappush(minHeap, (newCost, (newRow, newCol)))

        return maxCost
