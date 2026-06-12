# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        slow, fast = head, head
        length = 0
        supportHash = {}

        while fast and fast.next:
            supportHash[length] = fast.val
            supportHash[length + 1] = fast.next.val
            length += 2
            fast = fast.next.next
            slow = slow.next
        
        print(f"{supportHash}")
        middle = length//2
        maxSum = 0
        for index in range(0, middle):
            currentSum = supportHash[middle + index] + supportHash[middle - (index + 1)]
            if currentSum > maxSum:
                maxSum = currentSum

        return maxSum