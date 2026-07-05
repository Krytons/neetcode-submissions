import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #STEP 1 -- Convert times to an adjacency list
        adjList = {}
        for number in range (1, n +1):
            adjList[number] = []
        for start, destination, weigth in times:
            adjList[start].append((destination, weigth))
        
        #STEP 2 -- Initialize the min heap and result hashmap
        minheap = [(0, k)]
        result = {}
        lastnode = k

        #STEP 3 -- Core algorithm 
        while minheap:
            cost, node = heapq.heappop(minheap)
            if node in result:
                continue
            result[node] = cost
            lastnode = node
            print(f"Added {node} with cost of {cost}")
            
            for destination, weigth in adjList[node]:
                if destination not in result:
                    heapq.heappush(minheap, (weigth + cost, destination))

        return result[lastnode] if len(result) == n else -1
