# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        condition = True;
        currentNode = root;
        if currentNode == None:
            return TreeNode(val, None, None)

        while condition:
            if currentNode.val == val:
                return root;
            elif val < currentNode.val:
                if currentNode.left == None:
                    newNode = TreeNode(val, None, None)
                    currentNode.left = newNode
                    return root
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right == None:
                    newNode = TreeNode(val, None, None)
                    currentNode.right = newNode
                    return root
                else:
                    currentNode = currentNode.right


        
        