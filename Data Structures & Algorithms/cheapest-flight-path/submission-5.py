import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        #STEP 1 -- Build adj List
        adjList = {}
        for fromAirpoirt, toAirport, price in flights:
            if fromAirpoirt not in adjList:
                adjList[fromAirpoirt] = []
            if toAirport not in adjList:
                adjList[toAirport] = []
            adjList[fromAirpoirt].append((toAirport, price))

        #STEP 2 -- Generate minheap
        bestCosts = [[math.inf] * (k + 2) for _ in range(n)]
        bestCosts[src][0] = 0
        minHeap = []
        heapq.heappush(minHeap, (0, src, 0))

        #STEP 3 -- Dijkstra for min cost starting from src
        while minHeap:
            currentCost, currentAirport, flightUsed = heapq.heappop(minHeap)
            
            #Reached destination or reached max flights possible
            if currentAirport is dst:
                return currentCost

            if flightUsed > k or currentCost > bestCosts[currentAirport][flightUsed]:
                continue

            #At end, add possibile flights to minheap
            for destination, price in adjList[currentAirport]:
                newCost = currentCost + price
                if newCost < bestCosts[destination][flightUsed + 1]:
                    bestCosts[destination][flightUsed + 1] = newCost
                    heapq.heappush(minHeap, (newCost, destination, flightUsed + 1))
        
        return -1

            

            
