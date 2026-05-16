# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        last_visited = None
        cur = root
        heights = {}  

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            peek = stack[-1]
            if peek.right and last_visited is not peek.right:
                cur = peek.right
            else:
                left_h  = heights.get(peek.left, 0)
                right_h = heights.get(peek.right, 0)

                if abs(left_h - right_h) > 1:
                    return False

                heights[peek] = 1 + max(left_h, right_h)
                last_visited = stack.pop()

        return True