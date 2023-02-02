import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)
        self.median = 0.0

        

    def addNum(self, num):
        if self.max_heap == [] and self.min_heap == []:
            heapq.heappush(self.max_heap, num * -1)
        elif num > self.median:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, num * -1)
        if len(self.max_heap) - len(self.min_heap) == 2:
            new_val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, new_val * -1)
        elif len(self.min_heap) - len(self.max_heap) == 2:
            new_val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, new_val * -1)
        if len(self.min_heap) - len(self.max_heap) == 1:
            self.median = self.min_heap[0]
        elif len(self.max_heap) - len(self.min_heap) == 1:
            self.median = self.max_heap[0] * -1
        else:
            self.median = (self.min_heap[0] + (self.max_heap[0] * -1)) / 2

    def findMedian(self) -> float:
        # if len(self.min_heap) - len(self.max_heap) == 1:
        #     self.median = self.min_heap[0]
        # elif len(self.max_heap) - len(self.min_heap) == 1:
        #     self.median = self.max_heap[0] * -1
        # else:
        #     self.median = (self.min_heap[0] + (self.max_heap[0] * -1)) / 2
        return self.median
    
# medianFinder = MedianFinder()

# medianFinder.addNum(1)
# medianFinder.addNum(2)
# print(medianFinder.findMedian()) # 1.5
# medianFinder.addNum(3) 
# print(medianFinder.findMedian()) # 2
# medianFinder.addNum(4)
# medianFinder.addNum(5)
# medianFinder.addNum(6)
# print(medianFinder.findMedian()) # 3.5
# ============================================
# -2
medianFinder = MedianFinder()

medianFinder.addNum(0)
medianFinder.addNum(-1)
medianFinder.addNum(-2)
medianFinder.addNum(-3)
medianFinder.addNum(-4)
# print(medianFinder.findMedian()) # -2