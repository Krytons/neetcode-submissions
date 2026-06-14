class Union:
    def __init__(self, n):
        self.parents = {}
        self.rank = {}
        
        for number in range(1, n +1):
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        currentUnion = Union(len(edges))

        for edge in edges:
            if not currentUnion.union(edge[0], edge[1]):
                return edge

        return [0,0]

        