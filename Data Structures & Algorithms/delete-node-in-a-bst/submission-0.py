# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #STEP 1 -- Look for node to delete
        ancestor_stack = []
        current = root
        while current and current.val != key:
            ancestor_stack.append(current)
            current = current.right if key > current.val else current.left
        if not current:                            
            return root

        #STEP 2 -- Evaluate each case looking at delete node children
        target = current
        #CASE 2.A -- Both children 
        if target.left and target.right:
            ancestor_stack.append(target)
            inorder_successor = target.right #Start in order traversal to the significant part of the tree
            while inorder_successor.left:
                ancestor_stack.append(inorder_successor)
                inorder_successor = inorder_successor.left

            target.val = inorder_successor.val     
            successor_parent = ancestor_stack.pop()

            if successor_parent.left is inorder_successor:
                successor_parent.left = inorder_successor.right
            else:
                successor_parent.right = inorder_successor.right
            return root

        #CASE 2.B -- One or none children 
        replacement = target.left if target.left else target.right
        if not ancestor_stack: #Empty stack means that the removed node is the root                    
            return replacement

        target_parent = ancestor_stack.pop()
        if target_parent.left is target:
            target_parent.left = replacement
        else:
            target_parent.right = replacement
        return root
