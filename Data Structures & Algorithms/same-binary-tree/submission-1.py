# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        return self.inOrder(p) == self.inOrder(q)

    def inOrder(self, root: Optional[TreeNode]) -> list[int]: 
        stack = []
        visited = set()
        result = []
        currentNode = root

        while currentNode:
            while currentNode.val not in visited and currentNode.left:
                visited.add(currentNode.val)
                stack.append(currentNode)
                currentNode = currentNode.left

            if currentNode.val not in visited:
                result.append(currentNode.val)
                if currentNode.right:
                    stack.append(currentNode.right)
                
            currentNode = stack.pop() if stack else None

        return result
                    





