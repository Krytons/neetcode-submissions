# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []

        queue = [root]
        newqueue = []
        result = []
        while queue:
            currentResultValue = []
            newqueue = []
            for element in queue:
                currentResultValue.append(element.val)
                if element.left:
                    newqueue.append(element.left)
                if element.right:
                    newqueue.append(element.right)

            result.append(currentResultValue)
            queue = newqueue

        return result