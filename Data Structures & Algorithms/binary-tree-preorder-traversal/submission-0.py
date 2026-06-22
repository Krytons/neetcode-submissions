# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            currentNode = stack.pop()
            result.append(currentNode.val)

            if(currentNode.right):
                stack.append(currentNode.right)
            if(currentNode.left):
                stack.append(currentNode.left)

        return result

        