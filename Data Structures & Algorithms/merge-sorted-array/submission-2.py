class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        #STEP 1 -- Remove and re-attach zeros at the beginning of the list
        for loop in range(m, m+n):
            nums1.pop();
            nums1.insert(0, 0);
        
        #STEP 2 -- Initialize pointers and start the merge
        i = n
        j = 0
        for iteration in range(0, m+n):
            if i == m+n:
                nums1[iteration : m+n] = nums2[j : n]
                break;
            elif j == n:
                break;
            elif nums2[j] <= nums1[i]:
                nums1[iteration] = nums2[j]
                j += 1
            else:
                nums1[iteration] = nums1[i]
                i += 1


        