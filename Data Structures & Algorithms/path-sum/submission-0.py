# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
            
        stack = []
        lastVisited = None
        currentNode = root
        currentSum = 0
        while currentNode or stack:
            print(f"Current node is {currentNode} and total sum is {currentSum}")
            while currentNode:
                stack.append(currentNode)
                currentSum += currentNode.val
                currentNode = currentNode.left

            peekNode = stack[-1]
            if peekNode.right and lastVisited != peekNode.right:
                currentNode = peekNode.right
            else:
                lastVisited = stack.pop();
                if currentSum == targetSum and not lastVisited.left and not lastVisited.right:
                    return True
                else:
                    currentSum -= lastVisited.val

        return False;