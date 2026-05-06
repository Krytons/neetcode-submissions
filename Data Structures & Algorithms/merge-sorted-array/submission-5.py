class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1 #Num1 index
        j = n - 1 #Num2 index
        k = n + m - 1 #Overall tail index
        while k >= 0:
            if j < 0:
                break
            if i < 0:
                nums1[0:k+1] = nums2[0:j+1]
                break
            elif nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1


        