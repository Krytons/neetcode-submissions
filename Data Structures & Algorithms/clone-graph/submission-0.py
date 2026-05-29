"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        clone = {}
        stack = [node]

        while stack:
            currentNode = stack.pop()
            if currentNode.val not in clone:
                clone[currentNode.val] = Node(currentNode.val) 
            
            for neighbor in currentNode.neighbors:
                if neighbor.val not in clone:
                    clone[neighbor.val] = Node(neighbor.val) 
                    stack.append(neighbor)
                clone[currentNode.val].neighbors.append(clone[neighbor.val])

        return clone[1]