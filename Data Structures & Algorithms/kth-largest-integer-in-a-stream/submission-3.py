import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.heap = []
        for value in nums:
            self.add(value)
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k: 
            heapq.heappush(self.heap, val) 
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)

        return self.heap[0]

        
