# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        stack = [(root, False)]
        while stack:
            currentNode, isVisited = stack.pop()
            if isVisited:
                result.append(currentNode.val)
            else:
                stack.append((currentNode, True))  
                if (currentNode.right):
                  stack.append((currentNode.right, False))  
                if (currentNode.left):
                  stack.append((currentNode.left, False))  

        return result