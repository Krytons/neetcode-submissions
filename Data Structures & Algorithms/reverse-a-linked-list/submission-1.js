/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {
        let lastNode = null;
        let currentLastNode = null;
        while(head){ 
            currentLastNode = lastNode;
            lastNode = head;
            head = head.next;
            lastNode.next = currentLastNode;
        }
        return lastNode;
    }
}
