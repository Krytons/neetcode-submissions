import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] #This is a max heap
        self.big = [] #This is a min heap

    def addNum(self, num: int) -> None:
        #STEP 1 -- Push always to small
        heapq.heappush_max(self.small, num)

        #STEP 2 -- Check roots condition
        if (self.small and self.big and self.small[0] > self.big[0]):
            popped = heapq.heappop_max(self.small)
            heapq.heappush(self.big, num)

        #STEP 3 -- Handle heaps size
        slen = len(self.small)
        blen = len(self.big)
        if (slen > blen + 1):
            popped = heapq.heappop_max(self.small)
            heapq.heappush(self.big, popped)
        elif(blen > slen + 1):
            popped = heapq.heappop(self.big)
            heapq.heappush_max(self.small, popped)


    def findMedian(self) -> float:
        slen = len(self.small)
        blen = len(self.big)
        if slen == 0 and blen == 0:
            return 0
        elif (slen > blen):
            return self.small[0]
        elif(blen > slen):
            return self.big[0]
        else:
            return (self.small[0] + self.big[0]) / 2
        
        