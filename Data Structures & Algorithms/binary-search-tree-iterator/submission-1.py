# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iot = []
        if not root:
            return None

        self.pointer = math.nan
        stack = []
        currentNode = root
        while stack or currentNode:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left

            currentNode = stack.pop()
            print(f"Appending {currentNode.val}")
            self.iot.append(currentNode.val)
            currentNode = currentNode.right
          

    def next(self) -> int:
        if self.pointer is math.nan:
            self.pointer = 0
        elif self.pointer < len(self.iot):
            self.pointer += 1

        return self.iot[self.pointer]
        

    def hasNext(self) -> bool:
        if self.pointer is math.nan:
            return len(self.iot) > 0
        else:
            return self.pointer + 1 < len(self.iot)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()