import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #STEP 1 -- Build Adj List
        adj = {}
        for index in range(0, len(points)):
            adj[index] = []
            currentX, currentY = points[index]
            for subindex in range(0, len(points)):
                x,y = points[subindex]
                if currentX == x and currentY == y:
                    continue
                cost = abs(currentX - x) + abs(currentY - y)
                adj[index].append([subindex, cost])


        #STEP 2 -- Initialize Prim's
        minheap = []
        for neighbour, cost in adj[0]:
            heapq.heappush(minheap, (cost, 0, neighbour))
        visited = set()
        visited.add(0)
        output = 0


        #STEP 3 -- Execute Prim's
        while len(visited) <= len(points) - 1:
            cost, source, node = heapq.heappop(minheap)
            if node in visited:
                continue
            print(f'Visiting {node}, using a cost of {cost}')
            visited.add(node)
            output += cost

            for neighbour, ncost in adj[node]:
                if neighbour not in visited:
                    heapq.heappush(minheap, (ncost, node, neighbour))

        return output

        