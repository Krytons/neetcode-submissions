import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        if not edges or not succProb:
            return 0

        #STEP 1 -- Build adj list
        adjList = {}
        for index in range(0, len(edges)):
            currentProb = succProb[index]
            for node in edges[index]:
                if not node in adjList:
                    adjList[node] = []
            firstNode, secondNode = edges[index]
            adjList[firstNode].append((secondNode, currentProb))
            adjList[secondNode].append((firstNode, currentProb))

        #STEP 2 -- Initialize a maxheap
        maxHeap = [(1, start_node)]
        result = {}

        #STEP 3 -- 'Reverse' Dijkstra algorithm
        while maxHeap and not end_node in result:
            prob, node = heapq.heappop_max(maxHeap)
            if node not in result:
                result[node] = prob

            for connectedNode, connectedProb in adjList[node]:
                if connectedNode not in result:
                    heapq.heappush_max(maxHeap, (prob * connectedProb, connectedNode))

        return result[end_node] if end_node in result else 0

            
