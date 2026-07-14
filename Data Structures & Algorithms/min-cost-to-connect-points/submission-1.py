import heapq

class Union:
    def __init__(self, n):
        self.parents = {}
        self.rank = {}
        
        for number in range(0, n):
            self.parents[number] = number
            self.rank[number] = 0


    def find(self, n):
        parent = self.parents[n]
        while parent != self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]] #Shorten the path
            parent = self.parents[parent]
        return parent

    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False

        rank1, rank2 = self.rank[parent1], self.rank[parent2]
        if(rank1 > rank2):
            self.parents[parent2] = parent1
        if(rank1 < rank2):
            self.parents[parent1] = parent2
        else:
            self.parents[parent1] = parent2
            self.rank[parent2] += 1

        return True;

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = []
        for index in range(0, len(points)):
            currentX, currentY = points[index]
            for subindex in range(0, len(points)):
                x,y = points[subindex]
                if currentX == x and currentY == y:
                    continue
                cost = abs(currentX - x) + abs(currentY - y)
                heapq.heappush(minheap, (cost, index, subindex))
        
        unionFind = Union(len(points))
        visited = set()
        result = 0

        while len(visited) < len(points) -1:
            cost, source, node = heapq.heappop(minheap)
            if not unionFind.union(source, node):
                continue

            result += cost
            visited.add((source,node))

        return result



        """
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
        """

        