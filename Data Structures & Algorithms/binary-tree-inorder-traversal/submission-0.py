# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = []
        result = []
        currentNode = root
        while currentNode or stack:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left

            currentNode = stack.pop()
            result.append(currentNode.val)

            currentNode = currentNode.right

        return result