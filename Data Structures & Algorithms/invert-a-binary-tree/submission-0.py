# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
            
        currentQueue = []
        result = []
        currentQueue.append(root)

        while currentQueue:
            currentNode = currentQueue.pop()
            if currentNode.left:
                currentQueue.append(currentNode.left)
            if currentNode.right: 
                currentQueue.append(currentNode.right)

            currentNode.left, currentNode.right = currentNode.right, currentNode.left
            

        return root


