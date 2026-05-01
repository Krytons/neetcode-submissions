/**
 * class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}
 * 
 */
 


class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        if (!list1) 
            return list2;
        if (!list2) 
            return list1;

        if(list1.val > list2.val){
            console.log('Value %s is bigger than %s', list1?.val, list2?.val);
            list2.next = this.mergeTwoLists(list2.next, list1);
            return list2;
        }
        else{
            console.log('Value %s is bigger than %s', list2?.val, list1?.val);
            list1.next = this.mergeTwoLists(list1.next, list2);
            return list1;
        }
    }
}
