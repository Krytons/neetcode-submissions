import random

class KthLargest:

    def quickSort(self, nums):
        stack = [(0, len(nums) - 1)]

        while stack:
            lo, hi = stack.pop()
            if lo >= hi:
                continue

            pivotIdx = random.randint(lo, hi)
            nums[hi], nums[pivotIdx] = nums[pivotIdx], nums[hi] #Now pivot is at hi
            i = lo - 1
            for j in range(lo, hi):
                if nums[j] <= nums[hi]:      
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            i += 1
            nums[i], nums[hi] = nums[hi], nums[i]  #Nov pivot is at i position

            if i - lo > hi - i:              
                stack.append((lo, i - 1))
                stack.append((i + 1, hi))
            else:
                stack.append((i + 1, hi))
                stack.append((lo, i - 1))
            

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.quickSort(nums)
        self.ordNums = nums
        
        
    def add(self, val: int) -> int:
        if(len(self.ordNums) == 0):
            self.ordNums.append(val)
            return val

        mid = 0
        lo = 0
        hi = len(self.ordNums) - 1
        print(f'Adding {val}')
        print(f'Current array {self.ordNums}')
        while lo <= hi:
            print(f'Low {lo}. High {hi}')
            mid = ((lo + hi) // 2);
            print(f'New mid {mid}')
            if (val >= self.ordNums[mid]):
                lo = mid + 1
            else:
                hi = mid - 1

        if (val >= self.ordNums[mid]):
            self.ordNums.insert(mid + 1, val)
        else:
            self.ordNums.insert(mid, val)
        return self.ordNums[-self.k]

        
