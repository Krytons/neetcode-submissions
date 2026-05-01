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
            console.log('Current last node is %s', currentLastNode ? currentLastNode.val : 'undefined');
            lastNode = head;
            console.log('New last node is %s', lastNode?.val);
            head = head.next;
            console.log('New head is %s', head?.val);
            lastNode.next = currentLastNode;
        }

        console.log('Returning new head %s', lastNode);
        return lastNode;
    }
}
