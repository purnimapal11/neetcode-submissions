class MedianFinder:

    def __init__(self):

        self.minheap = [] #larger values
        self.maxheap = [] #smaller values

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -1*num)

        if len(self.minheap) + 1 < len(self.maxheap):
            val = -1*heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)
        if len(self.minheap) > 1 + len(self.maxheap):
            val = -1 * heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, val)
        

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.maxheap) > len(self.minheap):
            return -1*self.maxheap[0]
        else:
            return (-1 * self.maxheap[0] + self.minheap[0])/2.0
        
        